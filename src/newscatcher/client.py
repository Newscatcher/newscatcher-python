"""
Newscatcher SDK client with custom methods for unlimited article retrieval.

This file extends the base clients with methods that chunk requests to overcome
the 10,000 article limit in both synchronous and asynchronous implementations.
"""

import sys
import os
import datetime
import asyncio
import re
from typing import Dict, List, Optional, Union, Any, Set, Tuple, Callable

from .base_client import BaseNewscatcherApi, AsyncBaseNewscatcherApi
from .types.articles import Articles
from .utils import (
    parse_time_parameters,
    create_time_chunks,
    setup_progress_tracking,
    format_datetime,
    calculate_when_param,
    safe_get_articles,
)


class QueryValidator:
    """
    Query validation utility implementing server-side validation logic.

    This class encapsulates all query validation rules to ensure consistency
    with the API's validation behavior and provide early error detection.
    """

    def __init__(self):
        """Initialize validator with validation rules."""
        self.not_allowed_characters = [
            "[",
            "]",
            "/",
            "\\",
            "%5B",
            "%5D",
            "%2F",
            "%5C",
            ":",
            "%3A",
            "^",
            "%5E",
        ]
        self.open_char = ["(", "%28"]
        self.close_char = [")", "%29"]

    def validate_query(self, query: str) -> Tuple[bool, str]:
        """
        Validate search query syntax according to API rules.

        Args:
            query: Search query string to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(query, str):
            return False, "Query must be a string"

        if not query.strip():
            return False, "Query cannot be empty"

        validation_checks = [
            self._check_allowed_characters,
            self._check_asterisk,
            self._check_start_end,
            self._check_middle,
            self._check_quotes,
        ]

        for check in validation_checks:
            is_valid, error_message = check(query)
            if not is_valid:
                return False, error_message

        return True, ""

    def _check_allowed_characters(self, query: str) -> Tuple[bool, str]:
        """Check for forbidden characters."""
        for char in self.not_allowed_characters:
            if char in query:
                return (
                    False,
                    f"Query parameter must not include following characters "
                    f"{str(self.not_allowed_characters)}. Please remove them from query parameter",
                )
        return True, ""

    def _check_asterisk(self, query: str) -> Tuple[bool, str]:
        """Check wildcard (*) usage rules."""
        if query == "*":
            return True, ""

        # Check for patterns that are invalid:
        # ^[\*]*$ - query that is only asterisks (but not single *)
        # [\s]\* - space followed by asterisk
        # ^\*[^\s] - asterisk at start followed by non-space
        matches = re.search(r"^[\*]{2,}$|[\s]\*|^\*[^\s]", query)
        if matches:
            return (
                False,
                "The wildcard (*) character in query parameter must be preceded "
                "by at least one alphabet or number. Please modify the query.",
            )
        return True, ""

    def _check_start_end(self, query: str) -> Tuple[bool, str]:
        """Check for invalid operators at query boundaries."""
        # Operators that cannot appear at the end
        end_operators = [
            "OR ",
            "%7C%7C",
            "%7C%7C ",
            "AND ",
            "%26%26",
            "%26%26 ",
            "&&",
            "&& ",
            "||",
            "|| ",
            "NOT",
            "NOT ",
            "%21",
            "%21 ",
            "!",
            "! ",
            "%2B",
            "%2B ",
            "-",
            "- ",
            "OR(",
            "OR (",
            "%7C%7C(",
            "%7C%7C (",
            "AND(",
            "AND( ",
            "%26%26(",
            "%26%26 (",
            "&&(",
            "&& (",
            "||(",
            "|| (",
            "OR )",
            "%7C%7C)",
            "%7C%7C )",
            "AND )",
            "%26%26)",
            "%26%26 )",
            "&&)",
            "&& )",
            "||)",
            "|| )",
        ]

        # Operators that cannot appear at the start
        start_operators = [
            "OR ",
            "OR",
            "%7C%7C",
            "AND ",
            "AND",
            "%26%26",
            "&&",
            "||",
            "NOT ",
            "NOT",
            "!",
            "%21",
            "-",
            "+",
            "%2B",
        ]

        # Check end operators
        for op in end_operators:
            if query.endswith(op):
                return (
                    False,
                    f"Query parameter ends with an operator {str(op)}. "
                    f"Please remove an unused operator.",
                )

        # Check start operators
        for op in start_operators:
            if query.startswith(op):
                return (
                    False,
                    f"Query parameter starts with an operator {str(op)}. "
                    f"The query must not start with such operator. Please remove it.",
                )

        return True, ""

    def _check_middle(self, query: str) -> Tuple[bool, str]:
        """Check for invalid operator combinations."""
        invalid_combinations = [
            " OR OR ",
            "%7C%7C %7C%7C",
            "|| ||",
            "|| (||",
            "||) ||",
            " AND AND ",
            "%26%26 %26%26",
            "&& &&",
            "&& (&&",
            "&&) &&",
            " NOT NOT ",
            "! !",
            "%21 %21",
            "- -",
            "--",
            " OR AND ",
            " AND OR ",
            "%7C%7C %26%26",
            "%26%26 %7C%7C",
            " OR (AND ",
            " AND (OR ",
            "%7C%7C (%26%26",
            "%26%26 (%7C%7C",
            " OR) AND ",
            " AND) OR ",
            "%7C%7C) %26%26",
            "%26%26) %7C%7C",
            "()",
        ]

        for combo in invalid_combinations:
            if combo in query:
                return (
                    False,
                    f'Query parameter contains operator " {str(combo)} " used without '
                    f"keywords. Please add keywords or remove one of the operators",
                )

        return True, ""

    def _check_quotes(self, query: str) -> Tuple[bool, str]:
        """Check for balanced quotes and parentheses."""
        # Check parentheses balance
        all_open = []
        all_closed = []

        for i in self.open_char:
            all_open.extend(re.findall(re.escape(i), query))
        for j in self.close_char:
            all_closed.extend(re.findall(re.escape(j), query))

        if len(all_open) != len(all_closed):
            return (
                False,
                'Query parameter contains an unclosed round bracket "(" or ")". '
                "Please close the bracket before proceeding.",
            )

        # Check quotes
        all_quotes = []
        for o in ['"', "%22"]:
            all_quotes.extend(re.findall(re.escape(o), query))

        if len(all_quotes) % 2 != 0:
            return (
                False,
                'Query parameter contains an unclosed quote ("). '
                "Please close the quote before proceeding.",
            )

        return True, ""


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

        # Check if running in a test environment
        is_test = "pytest" in sys.modules or "TEST_MODE" in os.environ

        chunks_iter = setup_progress_tracking(
            time_chunks,
            kwargs.get("show_progress", False),
            description=desc,
            is_test=is_test,  # Pass test flag
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

    def validate_query(self, query: str) -> Tuple[bool, str]:
        """
        Validate search query syntax locally before making API calls.

        This method implements the same validation logic as the server-side API
        to catch syntax errors early and reduce unnecessary API calls that would
        fail due to malformed queries.

        Args:
            query: The search query string to validate

        Returns:
            Tuple of (is_valid: bool, error_message: str)
            - If valid: (True, "")
            - If invalid: (False, "detailed error message")

        Examples:
            Basic validation:
            >>> is_valid, error = client.validate_query("python programming")
            >>> if not is_valid:
            ...     print(f"Query error: {error}")

            Complex boolean query:
            >>> is_valid, error = client.validate_query('("machine learning" OR AI) AND python')

            Bulk validation:
            >>> queries = ["valid query", "invalid [query]", "another AND valid"]
            >>> for q in queries:
            ...     is_valid, error = client.validate_query(q)
            ...     if not is_valid:
            ...         print(f"Invalid query '{q}': {error}")
        """
        # Initialize validator if not already done
        if not hasattr(self, "_query_validator"):
            self._query_validator = QueryValidator()
        return self._query_validator.validate_query(query)


# Synchronous implementation
class NewscatcherApi(BaseNewscatcherApi, NewscatcherMixin):
    """
    Extended Newscatcher API client with methods for comprehensive article retrieval
    and query validation.

    This class extends the base client by adding methods that automatically
    chunk requests by time to overcome API limitations, and provides local
    query validation to catch syntax errors before making API calls.
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
        validate_query: bool = True,  # New parameter for query validation
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
            validate_query: Whether to validate query syntax before making API calls
            **kwargs: Additional parameters to pass to the search.post method
                    (Any valid parameters for the search endpoint)

        Returns:
            List of Article objects

        Raises:
            ValueError: If validate_query=True and the query has invalid syntax

        Examples:
            ```python
            # Get articles about renewable energy from the last 7 days
            articles = client.get_all_articles(
                q="renewable energy",
                from_="7d",  # Last 7 days
                time_chunk_size="1h",  # Split into 1-hour chunks
                max_articles=50000     # Limit to 50,000 articles
            )

            # Disable query validation if needed
            articles = client.get_all_articles(
                q="complex [query] with special chars",
                validate_query=False  # Skip validation
            )
            ```
        """
        # Validate query syntax if enabled
        if validate_query:
            is_valid, error_message = self.validate_query(q)
            if not is_valid:
                raise ValueError(f"Invalid query syntax: {error_message}")

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
                    q=q,
                    from_=chunk_from,
                    to=chunk_to,
                    page=1,
                    page_size=100,  # Use maximum page size for efficiency
                    **request_params,
                )

                # Get the data from response
                if hasattr(first_page_response, "articles"):
                    articles_data = first_page_response.articles
                else:
                    # Handle different response structures
                    articles_data = getattr(first_page_response, "data", [])

                # Process articles from first page
                processed, current_count, should_continue = self._process_articles(
                    articles_data, seen_ids, deduplicate, max_articles, current_count
                )
                all_articles.extend(processed)

                # If we've hit the limit, stop processing
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Check if there are more pages
                total_pages = getattr(first_page_response, "total_pages", 1)

                # Fetch remaining pages if available
                for page in range(2, total_pages + 1):
                    if not should_continue:
                        break

                    page_response = self.search.post(
                        q=q,
                        from_=chunk_from,
                        to=chunk_to,
                        page=page,
                        page_size=100,
                        **request_params,
                    )

                    # Get articles from this page
                    if hasattr(page_response, "articles"):
                        page_articles = page_response.articles
                    else:
                        page_articles = getattr(page_response, "data", [])

                    # Process articles from this page
                    processed, current_count, should_continue = self._process_articles(
                        page_articles,
                        seen_ids,
                        deduplicate,
                        max_articles,
                        current_count,
                    )
                    all_articles.extend(processed)

                    # Stop if we've reached the limit
                    if not should_continue:
                        if show_progress:
                            print(
                                f"\nReached maximum article limit ({max_articles}). Stopping."
                            )
                        break

            except Exception as e:
                # Log the error but continue with other chunks
                if show_progress:
                    print(
                        f"Error processing chunk {chunk_from} to {chunk_to}: {str(e)}"
                    )
                continue

            # Update progress
            if show_progress:
                self.log_completion(show_progress, current_count)

        return all_articles

    def get_all_headlines(
        self,
        when: str = "7d",
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        **kwargs,
    ) -> Articles:
        """
        Fetch latest headlines by splitting the request into multiple time-based chunks
        to overcome the 10,000 article limit.

        This method works similarly to get_all_articles but specifically for the
        latest headlines endpoint, dividing the time range into smaller chunks
        and making multiple API calls.

        Args:
            when: Time period to search (e.g., '7d', '24h', '1d')
            time_chunk_size: Size of time chunks to divide the search (e.g., "1d", "12h")
                           Supported units: d (days), h (hours)
            max_articles: Maximum number of articles to return (defaults to DEFAULT_MAX_ARTICLES)
            show_progress: Whether to show a progress indicator
            deduplicate: Whether to remove duplicate articles (based on article ID)
            **kwargs: Additional parameters to pass to the latestheadlines.post method

        Returns:
            List of Article objects

        Examples:
            ```python
            # Get all technology headlines from the past week
            headlines = client.get_all_headlines(
                when="7d",
                time_chunk_size="1h",
                show_progress=True
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
            # Calculate when parameter for this chunk
            when_param = calculate_when_param(chunk_start, chunk_end)

            # Prepare request parameters
            request_params = self.prepare_request_params(kwargs)

            try:
                # Fetch first page to get total hits and pagination info
                first_page_response = self.latestheadlines.post(
                    when=when_param, page=1, **request_params
                )

                # Get articles safely from first page response
                articles_data = safe_get_articles(first_page_response)

                # Process articles from first page if any were found
                if articles_data:
                    processed_articles, current_count, should_continue = (
                        self._process_articles(
                            articles_data,  # Use the safely retrieved articles
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

                # Check if there are more pages
                total_pages = getattr(first_page_response, "total_pages", 1)

                # Stop processing if we've reached the limit
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # If there are more pages, fetch them
                if total_pages > 1:
                    for page in range(2, total_pages + 1):
                        try:
                            page_response = self.latestheadlines.post(
                                when=when_param, page=page, **request_params
                            )

                            # Get articles safely from page response
                            page_articles = safe_get_articles(page_response)

                            # Process articles if any were found
                            if page_articles:
                                processed_articles, current_count, should_continue = (
                                    self._process_articles(
                                        page_articles,  # Use the safely retrieved articles
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
    Extended async Newscatcher API client with methods for comprehensive article retrieval
    and query validation.

    This class extends the async base client by adding methods that automatically
    chunk requests by time to overcome API limitations, and provides local
    query validation to catch syntax errors before making API calls.
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
            client_method: The client method to call for each page
            params: Parameters to pass to the client method
            total_pages: Total number of pages to process
            concurrency: Maximum number of concurrent requests

        Returns:
            List of articles from all pages
        """
        # Create semaphore for concurrency control
        semaphore = asyncio.Semaphore(concurrency)

        async def fetch_page(page_num):
            async with semaphore:
                page_params = {**params, "page": page_num}
                return await client_method(**page_params)

        # Create tasks for all pages (starting from page 2)
        tasks = [fetch_page(page) for page in range(2, total_pages + 1)]

        # Execute with concurrency control
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        # Collect articles from all responses
        all_page_articles = []
        for response in responses:
            if isinstance(response, Exception):
                print(f"Error in page request: {str(response)}")
                continue

            # Get articles safely from response
            page_articles = safe_get_articles(response)
            if page_articles:
                all_page_articles.extend(page_articles)

        return all_page_articles

    async def get_all_articles(
        self,
        q: str,
        from_: Optional[Union[datetime.datetime, str]] = None,
        to: Optional[Union[datetime.datetime, str]] = None,
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        validate_query: bool = True,  # New parameter for query validation
        concurrency: int = 3,
        **kwargs,
    ) -> Articles:
        """
        Async version: Fetch articles matching the search criteria by splitting the request into
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
            validate_query: Whether to validate query syntax before making API calls
            concurrency: Maximum number of concurrent requests for pagination
            **kwargs: Additional parameters to pass to the search.post method
                    (Any valid parameters for the search endpoint)

        Returns:
            List of Article objects

        Raises:
            ValueError: If validate_query=True and the query has invalid syntax

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
        # Validate query syntax if enabled
        if validate_query:
            is_valid, error_message = self.validate_query(q)
            if not is_valid:
                raise ValueError(f"Invalid query syntax: {error_message}")

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
                    q=q,
                    from_=chunk_from,
                    to=chunk_to,
                    page=1,
                    page_size=100,  # Use maximum page size for efficiency
                    **request_params,
                )

                # Get the data from response
                if hasattr(first_page_response, "articles"):
                    articles_data = first_page_response.articles
                else:
                    # Handle different response structures
                    articles_data = getattr(first_page_response, "data", [])

                # Process articles from first page
                processed, current_count, should_continue = (
                    await self._process_articles(
                        articles_data,
                        seen_ids,
                        deduplicate,
                        max_articles,
                        current_count,
                    )
                )
                all_articles.extend(processed)

                # If we've hit the limit, stop processing
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Check if there are more pages
                total_pages = getattr(first_page_response, "total_pages", 1)

                # Fetch remaining pages concurrently if available
                if total_pages > 1:
                    # Use the async page processing method
                    additional_articles = await self._process_page_requests_async(
                        self.search.post,
                        {
                            "q": q,
                            "from_": chunk_from,
                            "to": chunk_to,
                            **request_params,
                        },
                        total_pages,
                        concurrency,
                    )

                    # Process additional articles
                    processed, current_count, should_continue = (
                        await self._process_articles(
                            additional_articles,
                            seen_ids,
                            deduplicate,
                            max_articles,
                            current_count,
                        )
                    )
                    all_articles.extend(processed)

                    # Stop if we've reached the limit
                    if not should_continue:
                        if show_progress:
                            print(
                                f"\nReached maximum article limit ({max_articles}). Stopping."
                            )
                        break

            except Exception as e:
                # Log the error but continue with other chunks
                if show_progress:
                    print(
                        f"Error processing chunk {chunk_from} to {chunk_to}: {str(e)}"
                    )
                continue

            # Update progress
            if show_progress:
                self.log_completion(show_progress, current_count)

        return all_articles

    async def get_all_headlines(
        self,
        when: str = "7d",
        time_chunk_size: str = "1h",  # Default to 1 hour chunks
        max_articles: Optional[int] = None,  # None uses DEFAULT_MAX_ARTICLES
        show_progress: bool = False,
        deduplicate: bool = True,
        concurrency: int = 3,
        **kwargs,
    ) -> Articles:
        """
        Async version: Fetch latest headlines by splitting the request into multiple
        time-based chunks to overcome the 10,000 article limit.

        Args:
            when: Time period to search (e.g., '7d', '24h', '1d')
            time_chunk_size: Size of time chunks to divide the search (e.g., "1d", "12h")
                           Supported units: d (days), h (hours)
            max_articles: Maximum number of articles to return (defaults to DEFAULT_MAX_ARTICLES)
            show_progress: Whether to show a progress indicator
            deduplicate: Whether to remove duplicate articles (based on article ID)
            concurrency: Maximum number of concurrent requests for pagination
            **kwargs: Additional parameters to pass to the latestheadlines.post method

        Returns:
            List of Article objects

        Examples:
            ```python
            # Get all technology headlines from the past week
            headlines = await client.get_all_headlines(
                when="7d",
                time_chunk_size="1h",
                concurrency=5,
                show_progress=True
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
            # Calculate when parameter for this chunk
            when_param = calculate_when_param(chunk_start, chunk_end)

            # Prepare request parameters
            request_params = self.prepare_request_params(kwargs)

            try:
                # Fetch first page to get total hits and pagination info
                first_page_response = await self.latestheadlines.post(
                    when=when_param, page=1, **request_params
                )

                # Get articles safely from first page response
                articles_data = safe_get_articles(first_page_response)

                # Process articles from first page if any were found
                if articles_data:
                    processed_articles, current_count, should_continue = (
                        await self._process_articles(
                            articles_data,  # Use the safely retrieved articles
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

                # Check if there are more pages
                total_pages = getattr(first_page_response, "total_pages", 1)

                # Stop processing if we've reached the limit
                if not should_continue:
                    if show_progress:
                        print(
                            f"\nReached maximum article limit ({max_articles}). Stopping."
                        )
                    break

                # Fetch remaining pages concurrently if available
                if total_pages > 1:
                    # Use the async page processing method
                    additional_articles = await self._process_page_requests_async(
                        self.latestheadlines.post,
                        {"when": when_param, **request_params},
                        total_pages,
                        concurrency,
                    )

                    # Process additional articles
                    processed, current_count, should_continue = (
                        await self._process_articles(
                            additional_articles,
                            seen_ids,
                            deduplicate,
                            max_articles,
                            current_count,
                        )
                    )
                    all_articles.extend(processed)

                    # Stop if we've reached the limit
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
