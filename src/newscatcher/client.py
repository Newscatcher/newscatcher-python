"""
Newscatcher SDK client with custom methods for unlimited article retrieval.

This file extends the base clients with methods that chunk requests to overcome
the 10,000 article limit in both synchronous and asynchronous implementations.
"""

import datetime
import asyncio
from typing import Dict, List, Optional, Union, Any, Set, Tuple, Callable

from .base_client import BaseNewscatcherApi, AsyncBaseNewscatcherApi
from .types.articles import Articles
from .utils import (
    parse_time_parameters,
    create_time_chunks,
    setup_progress_tracking,
    format_datetime,
    calculate_when_param,
)


# Mixin class with shared functionality
class NewscatcherMixin:
    """
    Common functionality for both synchronous and asynchronous Newscatcher API clients.
    """

    # Constants
    DEFAULT_MAX_ARTICLES = 100000

    def prepare_time_chunks(self, endpoint_type, **kwargs):
        """
        Prepare time chunks for API requests.

        Args:
            endpoint_type: Either 'search' or 'latestheadlines'
            **kwargs: Parameters including time-related options

        Returns:
            Tuple of (from_date, to_date, time_chunks_iterator)
        """
        from_date, to_date, chunk_delta = parse_time_parameters(endpoint_type, **kwargs)
        time_chunks = create_time_chunks(from_date, to_date, chunk_delta)

        desc = (
            f"Fetching {'article' if endpoint_type == 'search' else 'headlines'} chunks"
        )
        chunks_iter = setup_progress_tracking(
            time_chunks, kwargs.get("show_progress", False), description=desc
        )

        return from_date, to_date, chunks_iter

    def prepare_request_params(self, params, endpoint_params=None):
        """
        Prepare optimized request parameters.

        Args:
            params: Original parameters dictionary
            endpoint_params: Additional endpoint-specific parameters

        Returns:
            Dictionary of optimized parameters
        """
        # Create a copy to avoid modifying the original
        request_params = {**params} if params else {}

        # Add endpoint-specific parameters if provided
        if endpoint_params:
            request_params.update(endpoint_params)

        # Remove pagination parameters as we'll handle them
        if "page" in request_params:
            del request_params["page"]

        # Set optimal page size if not specified
        if "page_size" not in request_params:
            request_params["page_size"] = 1000  # Use maximum page size for efficiency

        return request_params

    def log_completion(self, show_progress, article_count):
        """
        Log completion message if progress tracking is enabled.

        Args:
            show_progress: Whether progress tracking is enabled
            article_count: Number of articles retrieved
        """
        if show_progress:
            print(f"Retrieved {article_count} articles")


# Synchronous implementation
class NewscatcherApi(BaseNewscatcherApi, NewscatcherMixin):
    """
    Extended Newscatcher API client with methods for comprehensive article retrieval.

    This class extends the base client by adding methods that automatically
    chunk requests by time to overcome API limitations.
    """

    def _process_articles(
        self,
        articles: Articles,
        seen_ids: Set[str],
        deduplicate: bool,
        max_articles: Optional[int],
        current_count: int,
    ) -> Tuple[Articles, int, bool]:
        """
        Process articles with deduplication and respect maximum article limit.

        Args:
            articles: List of articles to process
            seen_ids: Set of already seen article IDs for deduplication
            deduplicate: Whether to remove duplicate articles
            max_articles: Maximum number of articles to collect
            current_count: Current count of collected articles

        Returns:
            Tuple of (processed_articles, new_count, should_continue)
        """
        processed_articles = []

        for article in articles:
            # Skip if this is a duplicate and deduplication is enabled
            if deduplicate and article.id in seen_ids:
                continue

            # Add to processed articles
            processed_articles.append(article)

            # Add ID to seen set if deduplication is enabled
            if deduplicate:
                seen_ids.add(article.id)

            # Increment count
            current_count += 1

            # Check if we've hit the max_articles limit
            if max_articles is not None and current_count >= max_articles:
                return processed_articles, current_count, False

        return processed_articles, current_count, True

    def get_all_articles(
        self,
        q: str,
        from_: Optional[Union[datetime.datetime, str]] = None,
        to: Optional[Union[datetime.datetime, str]] = None,
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        **kwargs,
    ) -> Articles:
        """
        Fetch articles matching the search criteria by splitting the request into
        multiple time-based chunks to overcome the 10,000 article limit.

        This method divides the time range into smaller chunks and makes multiple API calls
        to retrieve articles that match the search criteria, even beyond the 10,000
        article limit of a single search query.

        Args:
            q: Search query
            from_: Start date (ISO 8601 format, datetime object, or relative time like "7d")
            to: End date (ISO 8601 format, datetime object, or relative time like "1d")
            time_chunk_size: Size of time chunks to divide the search (e.g., "1d", "12h")
                           Supported units: d (days), h (hours)
            max_articles: Maximum number of articles to return (defaults to DEFAULT_MAX_ARTICLES)
            show_progress: Whether to show a progress indicator
            deduplicate: Whether to remove duplicate articles (based on article ID)
            **kwargs: Additional parameters to pass to the search.post method
                    (Any valid parameters for the search endpoint)

        Returns:
            List of Article objects

        Examples:
            ```python
            # Get articles about renewable energy from the last 7 days
            articles = client.get_all_articles(
                q="renewable energy",
                from_="7d",  # Last 7 days
                time_chunk_size="1h",  # Split into 1-hour chunks
                max_articles=50000     # Limit to 50,000 articles
            )
            ```
        """
        # Apply default max_articles if not specified
        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        # Parse and validate time parameters and get chunks
        _, to_date, chunks_iter = self.prepare_time_chunks(
            "search",
            from_=from_,
            to=to,
            time_chunk_size=time_chunk_size,
            show_progress=show_progress,
        )

        # Initialize result collection
        all_articles = []
        seen_ids: Set[str] = set()
        current_count = 0

        # Process each time chunk
        for chunk_start, chunk_end in chunks_iter:
            # Convert dates to ISO format for the API
            chunk_from = format_datetime(chunk_start)
            chunk_to = format_datetime(chunk_end)

            # Prepare request parameters
            request_params = self.prepare_request_params(kwargs)

            try:
                # Fetch first page to get total hits and pagination info
                first_page_response = self.search.post(
                    q=q, from_=chunk_from, to=chunk_to, page=1, **request_params
                )

                # Process first page of results
                processed_articles, current_count, should_continue = (
                    self._process_articles(
                        first_page_response.articles,
                        seen_ids,
                        deduplicate,
                        max_articles,
                        current_count,
                    )
                )

                all_articles.extend(processed_articles)

                # Stop if we've reached the limit
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Calculate total pages
                total_pages = first_page_response.total_pages

                # If there are more pages, fetch them
                if total_pages > 1:
                    for page in range(2, total_pages + 1):
                        try:
                            page_response = self.search.post(
                                q=q,
                                from_=chunk_from,
                                to=chunk_to,
                                page=page,
                                **request_params,
                            )

                            # Process this page of results
                            processed_articles, current_count, should_continue = (
                                self._process_articles(
                                    page_response.articles,
                                    seen_ids,
                                    deduplicate,
                                    max_articles,
                                    current_count,
                                )
                            )

                            all_articles.extend(processed_articles)

                            # Stop if we've reached the limit
                            if not should_continue:
                                if show_progress:
                                    print(
                                        f"\nReached maximum article limit ({max_articles}). Stopping."
                                    )
                                break

                        except Exception as e:
                            print(f"Error fetching page {page}: {str(e)}")
                            # Continue with partial results

                    # Stop processing chunks if we've reached the limit
                    if not should_continue:
                        break

            except Exception as e:
                print(f"Error processing chunk {chunk_start} to {chunk_end}: {str(e)}")
                # Continue with next chunk

        self.log_completion(show_progress, len(all_articles))
        return all_articles

    def get_all_headlines(
        self,
        when: Optional[Union[datetime.datetime, str]] = None,
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        **kwargs,
    ) -> Articles:
        """
        Fetch all latest headlines by splitting the request into
        multiple time-based chunks to overcome the 10,000 article limit.

        Args:
            when: How far back to fetch headlines (ISO 8601 format, datetime object, or relative time like "7d")
            time_chunk_size: Size of time chunks to divide the search (e.g., "1d", "12h")
                           Supported units: d (days), h (hours)
            max_articles: Maximum number of articles to return (defaults to DEFAULT_MAX_ARTICLES)
            show_progress: Whether to show a progress indicator
            deduplicate: Whether to remove duplicate articles (based on article ID)
            **kwargs: Additional parameters to pass to the latest headlines method
                    (Any valid parameters for the latestheadlines endpoint)

        Returns:
            List of Article objects

        Examples:
            ```python
            # Get all latest headlines about technology from the last 7 days
            articles = client.get_all_headlines(
                when="7d",
                topic="tech",
                time_chunk_size="1h",  # Split into 1-hour chunks
                max_articles=50000     # Limit to 50,000 articles
            )
            ```
        """
        # Apply default max_articles if not specified
        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        # Parse and validate time parameters and get chunks
        _, to_date, chunks_iter = self.prepare_time_chunks(
            "latestheadlines",
            when=when,
            time_chunk_size=time_chunk_size,
            show_progress=show_progress,
        )

        # Initialize result collection
        all_articles = []
        seen_ids: Set[str] = set()
        current_count = 0

        # Process each time chunk
        for chunk_start, chunk_end in chunks_iter:
            # Calculate the "when" parameter for this chunk
            when_param = calculate_when_param(to_date, chunk_start)

            # Prepare request parameters
            request_params = self.prepare_request_params(kwargs)

            try:
                # Fetch first page to get total hits and pagination info
                first_page_response = self.latestheadlines.post(
                    when=when_param, page=1, **request_params
                )

                # Process first page of results
                processed_articles, current_count, should_continue = (
                    self._process_articles(
                        first_page_response.articles,
                        seen_ids,
                        deduplicate,
                        max_articles,
                        current_count,
                    )
                )

                all_articles.extend(processed_articles)

                # Stop if we've reached the limit
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Calculate total pages
                total_pages = first_page_response.total_pages

                # If there are more pages, fetch them
                if total_pages > 1:
                    for page in range(2, total_pages + 1):
                        try:
                            page_response = self.latestheadlines.post(
                                when=when_param, page=page, **request_params
                            )

                            # Process this page of results
                            processed_articles, current_count, should_continue = (
                                self._process_articles(
                                    page_response.articles,
                                    seen_ids,
                                    deduplicate,
                                    max_articles,
                                    current_count,
                                )
                            )

                            all_articles.extend(processed_articles)

                            # Stop if we've reached the limit
                            if not should_continue:
                                if show_progress:
                                    print(
                                        f"\nReached maximum article limit ({max_articles}). Stopping."
                                    )
                                break

                        except Exception as e:
                            print(f"Error fetching page {page}: {str(e)}")
                            # Continue with partial results

                    # Stop processing chunks if we've reached the limit
                    if not should_continue:
                        break

            except Exception as e:
                print(f"Error processing chunk {chunk_start} to {chunk_end}: {str(e)}")
                # Continue with next chunk

        self.log_completion(show_progress, len(all_articles))
        return all_articles


# Asynchronous implementation
class AsyncNewscatcherApi(AsyncBaseNewscatcherApi, NewscatcherMixin):
    """
    Async version of the extended Newscatcher API client with methods for
    unlimited article retrieval.

    This class extends the async base client by adding methods that automatically
    chunk requests by time to overcome API limitations.
    """

    async def _process_articles(
        self,
        articles: Articles,
        seen_ids: Set[str],
        deduplicate: bool,
        max_articles: Optional[int],
        current_count: int,
    ) -> Tuple[Articles, int, bool]:
        """
        Process articles with deduplication and respect maximum article limit.

        Args:
            articles: List of articles to process
            seen_ids: Set of already seen article IDs for deduplication
            deduplicate: Whether to remove duplicate articles
            max_articles: Maximum number of articles to collect
            current_count: Current count of collected articles

        Returns:
            Tuple of (processed_articles, new_count, should_continue)
        """
        processed_articles = []

        for article in articles:
            # Skip if this is a duplicate and deduplication is enabled
            if deduplicate and article.id in seen_ids:
                continue

            # Add to processed articles
            processed_articles.append(article)

            # Add ID to seen set if deduplication is enabled
            if deduplicate:
                seen_ids.add(article.id)

            # Increment count
            current_count += 1

            # Check if we've hit the max_articles limit
            if max_articles is not None and current_count >= max_articles:
                return processed_articles, current_count, False

        return processed_articles, current_count, True

    async def _process_page_requests_async(
        self,
        client_method: Callable,
        params: Dict[str, Any],
        total_pages: int,
        concurrency: int = 3,
    ) -> Articles:
        """
        Process multiple pages of results concurrently.

        Args:
            client_method: Async method to call for each page
            params: Base parameters to pass to the method
            total_pages: Total number of pages to request
            concurrency: Maximum number of concurrent requests

        Returns:
            List of Article objects from all pages
        """
        all_articles = []

        # Skip page 1 as it's already been fetched
        remaining_pages = list(range(2, total_pages + 1))

        # Process pages in batches to limit concurrency
        for batch_start in range(0, len(remaining_pages), concurrency):
            batch_pages = remaining_pages[batch_start : batch_start + concurrency]

            # Create tasks for this batch
            tasks = []
            for page in batch_pages:
                # Create a copy of parameters with updated page number
                page_params = {**params, "page": page}
                tasks.append(client_method(**page_params))

            # Wait for all tasks in this batch to complete
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)

            # Process successful results
            for result in batch_results:
                if not isinstance(result, Exception):
                    all_articles.extend(result.articles)
                else:
                    print(f"Error fetching a page: {str(result)}")

        return all_articles

    async def get_all_articles(
        self,
        q: str,
        from_: Optional[Union[datetime.datetime, str]] = None,
        to: Optional[Union[datetime.datetime, str]] = None,
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        concurrency: int = 3,  # Default concurrency for page fetching
        **kwargs,
    ) -> Articles:
        """
        Async version: Fetch all articles matching the search criteria by splitting the request into
        multiple time-based chunks to overcome the 10,000 article limit.

        This method divides the time range into smaller chunks and makes multiple API calls
        to retrieve all articles that match the search criteria, even beyond the 10,000
        article limit of a single search query.

        Args:
            q: Search query
            from_: Start date (ISO 8601 format, datetime object, or relative time like "7d")
            to: End date (ISO 8601 format, datetime object, or relative time like "1d")
            time_chunk_size: Size of time chunks to divide the search (e.g., "1d", "12h")
                           Supported units: d (days), h (hours)
            max_articles: Maximum number of articles to return (defaults to DEFAULT_MAX_ARTICLES)
            show_progress: Whether to show a progress indicator
            deduplicate: Whether to remove duplicate articles (based on article ID)
            concurrency: Maximum number of concurrent requests for pagination
            **kwargs: Additional parameters to pass to the search.post method
                    (Any valid parameters for the search endpoint)

        Returns:
            List of Article objects

        Examples:
            ```python
            # Get all articles about renewable energy from the last 7 days
            articles = await client.get_all_articles(
                q="renewable energy",
                from_="7d",  # Last 7 days
                time_chunk_size="1h",  # Split into 1-hour chunks
                max_articles=50000     # Limit to 50,000 articles
            )
            ```
        """
        # Apply default max_articles if not specified
        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        # Parse and validate time parameters and get chunks
        _, to_date, chunks_iter = self.prepare_time_chunks(
            "search",
            from_=from_,
            to=to,
            time_chunk_size=time_chunk_size,
            show_progress=show_progress,
        )

        # Initialize result collection
        all_articles = []
        seen_ids: Set[str] = set()
        current_count = 0

        # Process each time chunk
        for chunk_start, chunk_end in chunks_iter:
            # Convert dates to ISO format for the API
            chunk_from = format_datetime(chunk_start)
            chunk_to = format_datetime(chunk_end)

            # Prepare request parameters
            request_params = self.prepare_request_params(kwargs)

            try:
                # Fetch first page to get total hits and pagination info
                first_page_response = await self.search.post(
                    q=q, from_=chunk_from, to=chunk_to, page=1, **request_params
                )

                # Process first page of results
                processed_articles, current_count, should_continue = (
                    await self._process_articles(
                        first_page_response.articles,
                        seen_ids,
                        deduplicate,
                        max_articles,
                        current_count,
                    )
                )

                all_articles.extend(processed_articles)

                # Stop if we've reached the limit
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Calculate total pages
                total_pages = first_page_response.total_pages

                # If there are more pages, fetch them concurrently
                if total_pages > 1:
                    # Create base parameters for page requests
                    base_params = {
                        "q": q,
                        "from_": chunk_from,
                        "to": chunk_to,
                        **request_params,
                    }

                    # Process pages concurrently
                    additional_articles = await self._process_page_requests_async(
                        self.search.post, base_params, total_pages, concurrency
                    )

                    # Process the additional articles
                    processed_articles, current_count, should_continue = (
                        await self._process_articles(
                            additional_articles,
                            seen_ids,
                            deduplicate,
                            max_articles,
                            current_count,
                        )
                    )

                    # Add articles from additional pages
                    all_articles.extend(processed_articles)

                    # Stop processing chunks if we've reached the limit
                    if not should_continue:
                        if show_progress:
                            print(
                                f"\nReached maximum article limit ({max_articles}). Stopping."
                            )
                        break

            except Exception as e:
                print(f"Error processing chunk {chunk_start} to {chunk_end}: {str(e)}")
                # Continue with next chunk

        self.log_completion(show_progress, len(all_articles))
        return all_articles

    async def get_all_headlines(
        self,
        when: Optional[Union[datetime.datetime, str]] = None,
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        concurrency: int = 3,  # Default concurrency for page fetching
        **kwargs,
    ) -> Articles:
        """
        Async version: Fetch all latest headlines by splitting the request into
        multiple time-based chunks to overcome the 10,000 article limit.

        Args:
            when: How far back to fetch headlines (ISO 8601 format, datetime object, or relative time like "7d")
            time_chunk_size: Size of time chunks to divide the search (e.g., "1d", "12h")
                           Supported units: d (days), h (hours)
            max_articles: Maximum number of articles to return (defaults to DEFAULT_MAX_ARTICLES)
            show_progress: Whether to show a progress indicator
            deduplicate: Whether to remove duplicate articles (based on article ID)
            concurrency: Maximum number of concurrent requests for pagination
            **kwargs: Additional parameters to pass to the latest headlines method
                    (Any valid parameters for the latestheadlines endpoint)

        Returns:
            List of Article objects

        Examples:
            ```python
            # Get all latest headlines about technology from the last 7 days
            articles = await client.get_all_headlines(
                when="7d",
                topic="tech",
                time_chunk_size="1h",  # Split into 1-hour chunks
                max_articles=50000     # Limit to 50,000 articles
            )
            ```
        """
        # Apply default max_articles if not specified
        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        # Parse and validate time parameters and get chunks
        _, to_date, chunks_iter = self.prepare_time_chunks(
            "latestheadlines",
            when=when,
            time_chunk_size=time_chunk_size,
            show_progress=show_progress,
        )

        # Initialize result collection
        all_articles = []
        seen_ids: Set[str] = set()
        current_count = 0

        # Process each time chunk
        for chunk_start, chunk_end in chunks_iter:
            # Calculate the "when" parameter for this chunk
            when_param = calculate_when_param(to_date, chunk_start)

            # Prepare request parameters
            request_params = self.prepare_request_params(kwargs)

            try:
                # Fetch first page to get total hits and pagination info
                first_page_response = await self.latestheadlines.post(
                    when=when_param, page=1, **request_params
                )

                # Process first page of results
                processed_articles, current_count, should_continue = (
                    await self._process_articles(
                        first_page_response.articles,
                        seen_ids,
                        deduplicate,
                        max_articles,
                        current_count,
                    )
                )

                all_articles.extend(processed_articles)

                # Stop if we've reached the limit
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Calculate total pages
                total_pages = first_page_response.total_pages

                # If there are more pages, fetch them concurrently
                if total_pages > 1:
                    # Create base parameters for page requests
                    base_params = {"when": when_param, **request_params}

                    # Process pages concurrently
                    additional_articles = await self._process_page_requests_async(
                        self.latestheadlines.post, base_params, total_pages, concurrency
                    )

                    # Process the additional articles
                    processed_articles, current_count, should_continue = (
                        await self._process_articles(
                            additional_articles,
                            seen_ids,
                            deduplicate,
                            max_articles,
                            current_count,
                        )
                    )

                    # Add articles from additional pages
                    all_articles.extend(processed_articles)

                    # Stop processing chunks if we've reached the limit
                    if not should_continue:
                        if show_progress:
                            print(
                                f"\nReached maximum article limit ({max_articles}). Stopping."
                            )
                        break

            except Exception as e:
                print(f"Error processing chunk {chunk_start} to {chunk_end}: {str(e)}")
                # Continue with next chunk

        self.log_completion(show_progress, len(all_articles))
        return all_articles
