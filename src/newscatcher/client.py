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
    """Query validation utility implementing server-side validation logic."""

    def __init__(self):
        """Initialize validator with validation rules."""
        self.not_allowed_characters = [
            "[", "]", "/", "\\", "%5B", "%5D", "%2F", "%5C", 
            ":", "%3A", "^", "%5E"
        ]
        self.open_char = ["(", "%28"]
        self.close_char = [")", "%29"]

    def validate_query(self, query: str) -> Tuple[bool, str]:
        """Validate search query syntax according to API rules."""
        if not isinstance(query, str):
            return False, "Query must be a string"

        # Check for empty query (but don't strip the query for validation)
        if not query.strip():
            return False, "[q] parameter should not empty"

        # Apply the same validation checks as elasticsearch_helper.py
        result, message = self._check_allowed_characters(query, "q")
        if not result:
            return False, message

        result, message = self._check_asterisk(query, "q")
        if not result:
            return False, message

        result, message = self._check_start_end(query, "q")
        if not result:
            return False, message

        result, message = self._check_middle(query, "q")
        if not result:
            return False, message

        result, message = self._check_quotes(query, "q")
        if not result:
            return False, message

        return True, ""

    def _check_allowed_characters(self, query: str, variable_name: str) -> Tuple[bool, str]:
        """Check the query for any unallowed characters."""
        # Special handling: allow \" for exact phrase escaping
        temp_query = query.replace('\\\"', '___ESCAPED_QUOTE___')
        
        if any(ext in temp_query for ext in self.not_allowed_characters):
            return (
                False,
                f"[{variable_name}] parameter must not include following characters "
                f"{str(self.not_allowed_characters)}. Please remove them from [{variable_name}] parameter"
            )
        return True, ""

    def _check_asterisk(self, query: str, variable_name: str) -> Tuple[bool, str]:
        """Check the query for proper asterisk usage."""
        if query == "*":
            return True, ""
        
        # Use original regex pattern but fix the multiple asterisk check
        matches = re.search(r"^[\*]{2,}$|[\s]\*|^\*[^\s]", query)
        if matches:
            return (
                False,
                f"The wildcard (*) character in [{variable_name}] parameter must be preceded "
                f"by at least one alphabet or number. Please modify the query."
            )
        return True, ""

    def _check_start_end(self, query: str, variable_name: str) -> Tuple[bool, str]:
        """Check for invalid operators at query boundaries."""
        # Operators that cannot appear at the end - include missing ones
        end_operators = [
            "OR ", "%7C%7C", "%7C%7C ", "AND ", "%26%26", "%26%26 ",
            "&&", "&& ", "||", "|| ", "NOT", "NOT ", "%21", "%21 ",
            "!", "! ", "%2B", "%2B ", "-", "- ", "OR(", "OR (",
            "%7C%7C(", "%7C%7C (", "AND(", "AND( ", "%26%26(",
            "%26%26 (", "&&(", "&& (", "||(", "|| (", "OR )",
            "%7C%7C)", "%7C%7C )", "AND )", "%26%26)", "%26%26 )",
            "&&)", "&& )", "||)", "|| )",
            # Add missing operators that API rejects
            "OR", "AND"
        ]

        # Operators that cannot appear at the start
        start_operators = [
            " OR", "%7C%7C", " %7C%7C", " AND", "%26%26", " %26%26",
            "&&", " &&", " ||", "||", "( OR", "(%7C%7C", "( %7C%7C",
            "( AND", "(%26%26", "( %26%26", "(&&", "( &&", "( ||",
            "(||", ")OR", ") OR", ")%7C%7C", ") %7C%7C", ")AND",
            ") AND", ")%26%26", ") %26%26", ")&&", ") &&", " )||", ") ||"
        ]

        # Check end operators
        for op in end_operators:
            if query.endswith(op):
                return (
                    False,
                    f"[{variable_name}] parameter ends with an operator {str(op)}. "
                    f"Please remove an unused operator."
                )

        # Special check for word operators at start (AND, OR, NOT followed by space)
        # These should return a different error message to match API behavior
        if re.match(r"^(AND|OR|NOT)\s", query, re.IGNORECASE):
            operator = re.match(r"^(AND|OR|NOT)", query, re.IGNORECASE).group(1)
            return (
                False,
                f"Syntax error in input : unexpected  \"{operator}\" at position 0!"
            )

        # Check other start operators
        for op in start_operators:
            if query.startswith(op):
                return (
                    False,
                    f"[{variable_name}] parameter starts with an operator {str(op)}. "
                    f"The query must not start with such operator. Please remove it."
                )

        return True, ""

    def _check_middle(self, query: str, variable_name: str) -> Tuple[bool, str]:
        """Check for invalid operator combinations."""
        invalid_combinations = [
            " OR OR ", "%7C%7C %7C%7C", "|| ||", "|| (||", "||) ||",
            " AND AND ", "%26%26 %26%26", "&& &&", "&& (&&", "&&) &&",
            " NOT NOT ", "! !", "%21 %21", "- -", "--", " OR AND ",
            " AND OR ", "%7C%7C %26%26", "%26%26 %7C%7C", " OR (AND ",
            " AND (OR ", "%7C%7C (%26%26", "%26%26 (%7C%7C", " OR) AND ",
            " AND) OR ", "%7C%7C) %26%26", "%26%26) %7C%7C", "()"
        ]

        for combo in invalid_combinations:
            if combo in query:
                return (
                    False,
                    f"[{variable_name}] parameter contains operator \" {str(combo)} \" used without "
                    f"keywords. Please add keywords or remove one of the operators"
                )

        return True, ""

    def _check_quotes(self, query: str, variable_name: str) -> Tuple[bool, str]:
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
                f"[{variable_name}] parameter contains an unclosed round bracket \"(\" or \")\". "
                f"Please close the bracket before proceeding."
            )

        # Check quotes
        all_quotes = []
        for o in ["\"", "%22"]:
            all_quotes.extend(re.findall(re.escape(o), query))

        if len(all_quotes) % 2 == 0:
            return True, ""  # Fixed: return "" instead of 0
        return (
            False,
            f"[{variable_name}] parameter contains an unclosed quote (\"). "
            f"Please close the quote before proceeding."
        )


class NewscatcherMixin:
    """Common functionality for both synchronous and asynchronous Newscatcher API clients."""

    DEFAULT_MAX_ARTICLES = 100000

    def __init__(self):
        """Initialize the mixin with shared components."""
        self.query_validator = QueryValidator()

    def validate_query(self, query: str) -> Tuple[bool, str]:
        """Validate query syntax using the QueryValidator."""
        return self.query_validator.validate_query(query)

    def prepare_time_chunks(self, endpoint_type, **kwargs):
        """Prepare time chunks for API requests."""
        from_date, to_date, chunk_delta = parse_time_parameters(endpoint_type, **kwargs)
        time_chunks = create_time_chunks(from_date, to_date, chunk_delta)

        desc = f"Fetching {'article' if endpoint_type == 'search' else 'headlines'} chunks"
        is_test = "pytest" in sys.modules or "TEST_MODE" in os.environ

        chunks_iter = setup_progress_tracking(
            time_chunks,
            kwargs.get("show_progress", False),
            description=desc,
            is_test=is_test,
        )

        return from_date, to_date, chunks_iter

    def prepare_request_params(self, params, endpoint_params=None):
        """Prepare optimized request parameters."""
        request_params = {**params} if params else {}

        if endpoint_params:
            request_params.update(endpoint_params)

        if "page" in request_params:
            del request_params["page"]

        if "page_size" not in request_params:
            request_params["page_size"] = 1000

        return request_params

    def _process_articles(self, articles_data, seen_ids, deduplicate, max_articles, current_count):
        """Process articles with deduplication and limits."""
        processed_articles = []
        
        for article in articles_data:
            if current_count >= max_articles:
                return processed_articles, current_count, False

            if deduplicate:
                article_id = getattr(article, "id", None)
                if article_id and article_id in seen_ids:
                    continue
                if article_id:
                    seen_ids.add(article_id)

            processed_articles.append(article)
            current_count += 1

        return processed_articles, current_count, True


class NewscatcherApi(BaseNewscatcherApi, NewscatcherMixin):
    """Synchronous Newscatcher API client with unlimited article retrieval."""

    def __init__(self, api_key: str):
        """Initialize the synchronous client."""
        BaseNewscatcherApi.__init__(self, api_key=api_key)
        NewscatcherMixin.__init__(self)

    def get_all_articles(
        self,
        q: str,
        from_: Optional[Union[str, datetime.datetime]] = None,
        to: Optional[Union[str, datetime.datetime]] = None,
        time_chunk_size: str = "1h",
        max_articles: Optional[int] = None,
        show_progress: bool = False,
        deduplicate: bool = True,
        validate_query: bool = True,
        concurrency: int = 5,
        **kwargs
    ) -> List[Any]:
        """Retrieve all articles matching search criteria, bypassing the 10,000 limit."""
        
        if validate_query:
            is_valid, error_message = self.validate_query(q)
            if not is_valid:
                raise ValueError(f"Invalid query syntax: {error_message}")

        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        from_date, to_date, chunks_iter = self.prepare_time_chunks(
            "search",
            from_=from_,
            to=to,
            time_chunk_size=time_chunk_size,
            show_progress=show_progress,
        )

        all_articles = []
        seen_ids: Set[str] = set()
        current_count = 0

        for chunk_start, chunk_end in chunks_iter:
            chunk_from = format_datetime(chunk_start)
            chunk_to = format_datetime(chunk_end)
            
            request_params = self.prepare_request_params(kwargs)

            try:
                first_page_response = self.search.post(
                    q=q,
                    from_=chunk_from,
                    to=chunk_to,
                    page=1,
                    **request_params
                )

                articles_data = safe_get_articles(first_page_response)

                if articles_data:
                    processed_articles, current_count, should_continue = (
                        self._process_articles(
                            articles_data,
                            seen_ids,
                            deduplicate,
                            max_articles,
                            current_count,
                        )
                    )

                    all_articles.extend(processed_articles)

                    if not should_continue:
                        if show_progress:
                            print(f"\nReached maximum article limit ({max_articles}).")
                        break

                    total_pages = getattr(first_page_response, "total_pages", 1)
                    
                    if total_pages > 1:
                        for page in range(2, min(total_pages + 1, 11)):
                            if current_count >= max_articles:
                                break

                            page_response = self.search.post(
                                q=q,
                                from_=chunk_from,
                                to=chunk_to,
                                page=page,
                                **request_params
                            )

                            page_articles = safe_get_articles(page_response)
                            if page_articles:
                                processed_articles, current_count, should_continue = (
                                    self._process_articles(
                                        page_articles,
                                        seen_ids,
                                        deduplicate,
                                        max_articles,
                                        current_count,
                                    )
                                )

                                all_articles.extend(processed_articles)

                                if not should_continue:
                                    break

            except Exception as e:
                if show_progress:
                    print(f"Error processing chunk {chunk_from} to {chunk_to}: {e}")
                continue

        if show_progress:
            print(f"\nCompleted: Retrieved {len(all_articles)} articles")

        return all_articles


class AsyncNewscatcherApi(AsyncBaseNewscatcherApi, NewscatcherMixin):
    """Asynchronous Newscatcher API client with unlimited article retrieval."""

    def __init__(self, api_key: str):
        """Initialize the asynchronous client."""
        AsyncBaseNewscatcherApi.__init__(self, api_key=api_key)
        NewscatcherMixin.__init__(self)

    async def get_all_articles(
        self,
        q: str,
        from_: Optional[Union[str, datetime.datetime]] = None,
        to: Optional[Union[str, datetime.datetime]] = None,
        time_chunk_size: str = "1h",
        max_articles: Optional[int] = None,
        show_progress: bool = False,
        deduplicate: bool = True,
        validate_query: bool = True,
        concurrency: int = 5,
        **kwargs
    ) -> List[Any]:
        """Asynchronously retrieve all articles matching search criteria."""
        
        if validate_query:
            is_valid, error_message = self.validate_query(q)
            if not is_valid:
                raise ValueError(f"Invalid query syntax: {error_message}")

        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        from_date, to_date, chunks_iter = self.prepare_time_chunks(
            "search",
            from_=from_,
            to=to,
            time_chunk_size=time_chunk_size,
            show_progress=show_progress,
        )

        all_articles = []
        seen_ids: Set[str] = set()
        current_count = 0

        for chunk_start, chunk_end in chunks_iter:
            chunk_from = format_datetime(chunk_start)
            chunk_to = format_datetime(chunk_end)
            
            request_params = self.prepare_request_params(kwargs)

            try:
                first_page_response = await self.search.post(
                    q=q,
                    from_=chunk_from,
                    to=chunk_to,
                    page=1,
                    **request_params
                )

                articles_data = safe_get_articles(first_page_response)

                if articles_data:
                    processed_articles, current_count, should_continue = (
                        self._process_articles(
                            articles_data,
                            seen_ids,
                            deduplicate,
                            max_articles,
                            current_count,
                        )
                    )

                    all_articles.extend(processed_articles)

                    if not should_continue:
                        if show_progress:
                            print(f"\nReached maximum article limit ({max_articles}).")
                        break

                    total_pages = getattr(first_page_response, "total_pages", 1)
                    
                    if total_pages > 1:
                        tasks = []
                        semaphore = asyncio.Semaphore(concurrency)
                        
                        async def fetch_page(page_num):
                            async with semaphore:
                                return await self.search.post(
                                    q=q,
                                    from_=chunk_from,
                                    to=chunk_to,
                                    page=page_num,
                                    **request_params
                                )

                        for page in range(2, min(total_pages + 1, 11)):
                            if current_count >= max_articles:
                                break
                            tasks.append(fetch_page(page))

                        if tasks:
                            page_responses = await asyncio.gather(*tasks, return_exceptions=True)
                            
                            for page_response in page_responses:
                                if isinstance(page_response, Exception):
                                    continue
                                    
                                if current_count >= max_articles:
                                    break

                                page_articles = safe_get_articles(page_response)
                                if page_articles:
                                    processed_articles, current_count, should_continue = (
                                        self._process_articles(
                                            page_articles,
                                            seen_ids,
                                            deduplicate,
                                            max_articles,
                                            current_count,
                                        )
                                    )

                                    all_articles.extend(processed_articles)

                                    if not should_continue:
                                        break

            except Exception as e:
                if show_progress:
                    print(f"Error processing chunk {chunk_from} to {chunk_to}: {e}")
                continue

        if show_progress:
            print(f"\nCompleted: Retrieved {len(all_articles)} articles")

        return all_articles