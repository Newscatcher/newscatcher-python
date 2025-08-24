import sys
import os
import datetime
import asyncio
import re
from typing import Optional, Union, List, Set, Tuple, Any

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

        # Apply the same validation checks as elasticsearch
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
        
        result, message = self._check_same_level_operators(query, "q")
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
    
    def _check_same_level_operators(self, query: str, variable_name: str) -> Tuple[bool, str]:
        """
        Check for AND/OR at same level after automatic AND insertion.
        
        The API automatically inserts AND operators between standalone terms that aren't 
        within quotes or connected by explicit operators. This creates same-level operator 
        violations when OR is mixed with these implicit ANDs.
        
        Examples:
        - "AI OR artificial intelligence" → "AI OR artificial AND intelligence" (INVALID)
        - "AI OR \"artificial intelligence\"" → "AI OR \"artificial intelligence\"" (VALID)
        """
        
        # Quick check: if no OR/AND operators, no same-level issue
        if not any(op in query for op in [' OR ', ' AND ', '||', '&&', '%7C%7C', '%26%26']):
            return True, ""
        
        # Tokenize the query while preserving quoted phrases and operators
        tokens = self._tokenize_query_for_same_level_check(query)
        
        # Simulate automatic AND insertion
        tokens_with_implicit_and = self._simulate_and_insertion(tokens)
        
        # Check for same-level AND/OR violations
        if self._has_same_level_and_or(tokens_with_implicit_and):
            return (
                False,
                f'in [{variable_name}] "AND" and "OR" operator not allowed at same level, '
                f'Please use parentheses to group terms correctly, such as '
                f'`(elon AND musk) OR twitter`.'
            )
        
        return True, ""

    def _tokenize_query_for_same_level_check(self, query: str) -> List[str]:
        """
        Tokenize query preserving quoted phrases, operators, and parentheses.
        
        Returns tokens like: ['AI', 'OR', 'artificial', 'intelligence'] 
        or ['AI', 'OR', '"artificial intelligence"']
        """
        tokens = []
        i = 0
        current_token = ""
        
        while i < len(query):
            char = query[i]
            
            # Handle quoted phrases (including escaped quotes)
            if char == '"':
                if current_token:
                    tokens.append(current_token.strip())
                    current_token = ""
                
                # Collect the entire quoted phrase
                quoted_phrase = '"'
                i += 1
                while i < len(query):
                    if query[i] == '"':
                        quoted_phrase += '"'
                        i += 1
                        break
                    elif query[i] == '\\' and i + 1 < len(query) and query[i + 1] == '"':
                        # Handle escaped quotes
                        quoted_phrase += query[i:i+2]
                        i += 2
                    else:
                        quoted_phrase += query[i]
                        i += 1
                
                tokens.append(quoted_phrase)
                continue
            
            # Handle operators and parentheses
            elif char in '()':
                if current_token:
                    tokens.append(current_token.strip())
                    current_token = ""
                tokens.append(char)
                i += 1
                continue
            
            # Handle spaces - potential token boundaries
            elif char == ' ':
                if current_token:
                    token = current_token.strip()
                    if token:
                        tokens.append(token)
                    current_token = ""
                i += 1
                continue
            
            else:
                current_token += char
                i += 1
        
        # Add final token
        if current_token:
            token = current_token.strip()
            if token:
                tokens.append(token)
        
        return tokens

    def _simulate_and_insertion(self, tokens: List[str]) -> List[str]:
        """
        Simulate automatic AND insertion between adjacent terms.
        
        Rules:
        - Insert AND between adjacent words that aren't operators
        - Don't insert AND around parentheses or quoted phrases
        - Don't insert AND if there's already an operator
        """
        if len(tokens) <= 1:
            return tokens
        
        result = []
        operators = {'AND', 'OR', 'NOT', '&&', '||', '%26%26', '%7C%7C', '!', '-'}
        brackets = {'(', ')'}
        
        for i, token in enumerate(tokens):
            result.append(token)
            
            # Check if we should insert AND after this token
            if i < len(tokens) - 1:
                current = token
                next_token = tokens[i + 1]
                
                # Don't insert AND if current or next is operator/bracket
                if (current.upper() in operators or 
                    next_token.upper() in operators or
                    current in brackets or 
                    next_token in brackets or
                    current.startswith('"') or  # Quoted phrase
                    next_token.startswith('"')):
                    continue
                
                # Insert implicit AND between standalone words
                if (not current.upper() in operators and 
                    not next_token.upper() in operators and
                    current not in brackets and 
                    next_token not in brackets):
                    result.append('AND')
        
        return result

    def _has_same_level_and_or(self, tokens: List[str]) -> bool:
        """
        Check if tokens contain AND/OR at the same precedence level.
        
        This is a simplified check that looks for AND and OR operators
        not properly separated by parentheses.
        """
        # Simple heuristic: if we have both AND and OR operators outside of 
        # properly grouped parentheses, it's likely a same-level violation
        
        has_and = any(token.upper() in ['AND', '&&', '%26%26'] for token in tokens)
        has_or = any(token.upper() in ['OR', '||', '%7C%7C'] for token in tokens)
        
        # If we have both AND and OR, we need to check grouping
        if has_and and has_or:
            # For now, use a simple heuristic: 
            # If there are no parentheses to group operations, assume violation
            if '(' not in tokens and ')' not in tokens:
                return True
            
            # More sophisticated parsing would check proper grouping
            # This is a basic implementation that catches common cases
            return self._check_operator_grouping(tokens)
        
        return False

    def _check_operator_grouping(self, tokens: List[str]) -> bool:
        """
        Check if AND/OR operators are properly grouped with parentheses.
        
        This is a simplified implementation that catches common violations.
        A full parser would be more accurate but more complex.
        """
        # Simple rule: if we see patterns like "term AND term OR term" without
        # parentheses properly separating the different operator types, it's invalid
        
        operators = []
        paren_depth = 0
        current_level_ops = []
        
        for token in tokens:
            if token == '(':
                # Starting new group - save current level operators
                if current_level_ops:
                    operators.append(current_level_ops.copy())
                current_level_ops = []
                paren_depth += 1
            elif token == ')':
                paren_depth -= 1
                # Check current level when closing group
                if len(set(current_level_ops)) > 1:  # Mixed operators at this level
                    return True
                current_level_ops = []
            elif token.upper() in ['AND', 'OR', '&&', '||', '%26%26', '%7C%7C']:
                normalized_op = 'AND' if token.upper() in ['AND', '&&', '%26%26'] else 'OR'
                current_level_ops.append(normalized_op)
        
        # Check final level
        return len(set(current_level_ops)) > 1

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
    
    def log_completion(self, show_progress: bool, article_count: int):
        """
        Log completion message if progress tracking is enabled.
        
        Args:
            show_progress: Whether progress tracking is enabled
            article_count: Number of articles retrieved
        """
        if show_progress:
            print(f"Retrieved {article_count} articles")


class NewscatcherApi(BaseNewscatcherApi, NewscatcherMixin):
    """Synchronous Newscatcher API client with unlimited article retrieval."""

    def __init__(self, api_key: str, **kwargs):
        """Initialize the synchronous client."""
        BaseNewscatcherApi.__init__(self, api_key=api_key, **kwargs)
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
        concurrency: int = 3,
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
    
    def get_all_headlines(
        self,
        when: Optional[Union[datetime.datetime, str]] = None,
        time_chunk_size: str = "1h",
        max_articles: Optional[int] = None,
        show_progress: bool = False,
        deduplicate: bool = True,
        **kwargs,
    ) -> Articles:
        """
        Fetch all latest headlines by splitting the request into
        multiple time-based chunks to overcome the 10,000 article limit.
        """
        
        # Set defaults
        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        # Parse time parameters - this converts when="1d" to proper time ranges
        from_date, to_date, chunk_delta = parse_time_parameters("latestheadlines", when=when, time_chunk_size=time_chunk_size)
        
        # Create time chunks
        time_chunks = create_time_chunks(from_date, to_date, chunk_delta)

        # Setup progress tracking
        desc = "Fetching headlines chunks"
        is_test = "pytest" in sys.modules or "TEST_MODE" in os.environ
        chunks_iter = setup_progress_tracking(
            time_chunks,
            show_progress,
            description=desc,
            is_test=is_test,
        )

        all_articles = []
        seen_ids = set()
        current_count = 0

        # Prepare request parameters
        request_params = {**kwargs}
        if "page" in request_params:
            del request_params["page"]
        if "page_size" not in request_params:
            request_params["page_size"] = 1000

        # Process each time chunk
        for chunk_start, chunk_end in chunks_iter:
            if current_count >= max_articles:
                break

            try:
                # Convert chunk times to the expected format using calculate_when_param
                when_param = calculate_when_param(chunk_end, chunk_start)  # This creates "1d", "2h", etc.

                # Make the first request
                first_response = self.latestheadlines.post(
                    when=when_param, page=1, **request_params
                )

                # Get articles safely from first response
                first_articles = safe_get_articles(first_response)

                if first_articles:
                    # Process first page articles
                    processed_articles, current_count, should_continue = (
                        self._process_articles(
                            first_articles,
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
                            print(f"\nReached maximum article limit ({max_articles}). Stopping.")
                        break

                    # Get total pages for pagination
                    total_pages = getattr(first_response, "total_pages", 1)
                    
                    # If there are more pages, fetch them
                    if total_pages > 1:
                        for page in range(2, min(total_pages + 1, 11)):
                            if current_count >= max_articles:
                                break

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
                                            page_articles,
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
                                            print(f"\nReached maximum article limit ({max_articles}). Stopping.")
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


class AsyncNewscatcherApi(AsyncBaseNewscatcherApi, NewscatcherMixin):
    """Asynchronous Newscatcher API client with unlimited article retrieval."""

    def __init__(self, api_key: str, **kwargs):
        """Initialize the asynchronous client."""
        AsyncBaseNewscatcherApi.__init__(self, api_key=api_key, **kwargs)
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
        concurrency: int = 3,
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
        """   
        # Set defaults
        if max_articles is None:
            max_articles = self.DEFAULT_MAX_ARTICLES

        # Parse time parameters
        from_date, to_date, chunk_delta = parse_time_parameters("latestheadlines", when=when, time_chunk_size=time_chunk_size)
        
        # Create time chunks
        time_chunks = create_time_chunks(from_date, to_date, chunk_delta)

        # Setup progress tracking
        desc = "Fetching headlines chunks"
        is_test = "pytest" in sys.modules or "TEST_MODE" in os.environ
        chunks_iter = setup_progress_tracking(
            time_chunks,
            show_progress,
            description=desc,
            is_test=is_test,
        )

        all_articles = []
        seen_ids = set()
        current_count = 0

        # Prepare request parameters
        request_params = {**kwargs}
        if "page" in request_params:
            del request_params["page"]
        if "page_size" not in request_params:
            request_params["page_size"] = 1000

        # Process each time chunk
        for chunk_start, chunk_end in chunks_iter:
            if current_count >= max_articles:
                break

            try:
                # Convert chunk times to the expected format using calculate_when_param  
                when_param = calculate_when_param(chunk_end, chunk_start)

                # Make the first request
                first_response = await self.latestheadlines.post(
                    when=when_param, page=1, **request_params
                )

                # Get articles safely from first response
                first_articles = safe_get_articles(first_response)

                if first_articles:
                    # Process first page articles
                    processed_articles, current_count, should_continue = (
                        self._process_articles(
                            first_articles,
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
                            print(f"\nReached maximum article limit ({max_articles}). Stopping.")
                        break

                    # Get total pages for pagination
                    total_pages = getattr(first_response, "total_pages", 1)
                    
                    # If there are more pages, fetch them with concurrency
                    if total_pages > 1:
                        page_tasks = []
                        semaphore = asyncio.Semaphore(concurrency)

                        async def fetch_page(page_num):
                            async with semaphore:
                                try:
                                    return await self.latestheadlines.post(
                                        when=when_param, page=page_num, **request_params
                                    )
                                except Exception as e:
                                    print(f"Error fetching page {page_num}: {str(e)}")
                                    return None

                        # Create tasks for all pages
                        for page in range(2, min(total_pages + 1, 11)):  # Limit to 10 pages max
                            if current_count >= max_articles:
                                break
                            page_tasks.append(fetch_page(page))

                        # Execute page requests with concurrency
                        if page_tasks:
                            page_responses = await asyncio.gather(*page_tasks, return_exceptions=True)

                            for response in page_responses:
                                if current_count >= max_articles:
                                    break

                                if response and not isinstance(response, Exception):
                                    page_articles = safe_get_articles(response)
                                    
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
                                            if show_progress:
                                                print(f"\nReached maximum article limit ({max_articles}). Stopping.")
                                            break

                        # Stop processing chunks if we've reached the limit
                        if not should_continue:
                            break

            except Exception as e:
                print(f"Error processing chunk {chunk_start} to {chunk_end}: {str(e)}")
                # Continue with next chunk

        self.log_completion(show_progress, len(all_articles))
        return all_articles