"""
Unit tests for query validation functionality.

Tests the QueryValidator class and validate_query method integration
with the NewsCatcher SDK clients.
"""

import pytest
import sys
import os
from unittest.mock import patch, Mock

# Add the src directory to the path for development testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

try:
    from newscatcher.client import NewscatcherApi, AsyncNewscatcherApi, QueryValidator
except ImportError:
    # Alternative import path if installed as package
    try:
        from newscatcher import NewscatcherApi, AsyncNewscatcherApi
        from newscatcher.client import QueryValidator
    except ImportError:
        pytest.skip("newscatcher package not available", allow_module_level=True)


class TestQueryValidator:
    """Test cases for the QueryValidator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_valid_queries(self):
        """Test queries that should pass validation."""
        valid_queries = [
            "simple query",
            'quoted "exact phrase"',
            "wildcard query term*",
            "boolean AND query",
            "(grouped OR terms)",
            "*",  # Special case: single asterisk is allowed
            'complex (query AND "exact phrase") OR wildcard*',
            "query with numbers 123",
            "query-with-hyphens",
            "query_with_underscores",
            "multiple* wild*cards",
            "nested (groups (within groups))",
            "boolean (python OR java) AND programming",
            "negation NOT spam",
            "complex -exclude +include terms",
        ]

        for query in valid_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                is_valid
            ), f"Query '{query}' should be valid but got error: {error_msg}"
            assert (
                error_msg == ""
            ), f"Valid query should have empty error message, got: '{error_msg}'"

    def test_forbidden_characters(self):
        """Test queries with forbidden characters."""
        forbidden_char_tests = [
            ("query[with]brackets", "["),
            ("query/with/slashes", "/"),
            ("query\\with\\backslashes", "\\"),
            ("query:with:colons", ":"),
            ("query^with^caret", "^"),
            ("query%5Bwith%5Dencoded", "%5B"),
            ("query%2Fwith%2Fencoded", "%2F"),
            ("query%5Cwith%5Cencoded", "%5C"),
            ("query%3Awith%3Aencoded", "%3A"),
            ("query%5Ewith%5Eencoded", "%5E"),
        ]

        for query, forbidden_char in forbidden_char_tests:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Query '{query}' should be invalid"
            assert "must not include following characters" in error_msg
            assert forbidden_char in error_msg

    def test_asterisk_validation(self):
        """Test asterisk/wildcard validation rules."""
        # Invalid asterisk usage
        invalid_asterisk_queries = [
            "*query",  # Asterisk at start
            "query *",  # Space before asterisk
            "***",  # Only asterisks (multiple)
            "** query",  # Multiple asterisks at start
            "query * term",  # Space before asterisk in middle
        ]

        for query in invalid_asterisk_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Query '{query}' should be invalid due to asterisk usage"
            assert "wildcard (*) character" in error_msg
            assert "preceded by at least one alphabet or number" in error_msg

        # Valid asterisk usage
        valid_asterisk_queries = [
            "*",  # Single asterisk (special case)
            "* query",  # Single asterisk with space after (should be valid)
            "term*",  # Asterisk after term
            "multiple* wild*cards",  # Multiple valid wildcards
            "query123*",  # Asterisk after numbers
        ]

        for query in valid_asterisk_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                is_valid
            ), f"Query '{query}' should be valid but got error: {error_msg}"

    def test_operator_start_end_validation(self):
        """Test validation of operators at start and end of queries."""
        # Invalid: operators at start (simplified list)
        invalid_start_queries = [
            "AND query",
            "&& query",
            "|| query",
            "NOT query",
            "! query",
            "- query",
            "+ query",
        ]

        for query in invalid_start_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Query '{query}' should be invalid - starts with operator"
            assert "starts with an operator" in error_msg

        # Invalid: operators at end
        invalid_end_queries = [
            "query OR ",
            "query AND ",
            "query &&",
            "query ||",
            "query NOT ",
            "query !",
            "query -",
        ]

        for query in invalid_end_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Query '{query}' should be invalid - ends with operator"
            assert "ends with an operator" in error_msg

        # Valid: operators in middle
        valid_operator_queries = [
            "query OR term",
            "search AND result",
            "term1 || term2",
            "word1 && word2",
            "python NOT tutorial",
        ]

        for query in valid_operator_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                is_valid
            ), f"Query '{query}' should be valid but got error: {error_msg}"

    def test_operator_combinations_validation(self):
        """Test validation of invalid operator combinations."""
        invalid_combinations = [
            "query OR OR term",  # Double OR
            "query AND AND term",  # Double AND
            "query NOT NOT term",  # Double NOT
            "query ! !",  # Double exclamation
            "query - -",  # Double minus
            "query --",  # Double dash
            "query OR AND term",  # OR AND combination
            "query AND OR term",  # AND OR combination
            "query ()",  # Empty parentheses
        ]

        for query in invalid_combinations:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Query '{query}' should be invalid due to operator combination"
            assert "used without keywords" in error_msg

    def test_quotes_and_parentheses_validation(self):
        """Test validation of balanced quotes and parentheses."""
        # Invalid: unbalanced quotes
        invalid_quote_queries = [
            'unbalanced "quote',
            'quote" unbalanced',
            'multiple "unbalanced "quotes"',
            "encoded%22unbalanced",
        ]

        for query in invalid_quote_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Query '{query}' should be invalid due to unbalanced quotes"
            assert "unclosed quote" in error_msg

        # Invalid: unbalanced parentheses
        invalid_paren_queries = [
            "unbalanced (parenthesis",
            "extra) parenthesis",
            "nested ((unbalanced)",
            "encoded%28unbalanced",
        ]

        for query in invalid_paren_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Query '{query}' should be invalid due to unbalanced parentheses"
            assert "unclosed round bracket" in error_msg

        # Valid: balanced quotes and parentheses
        valid_balanced_queries = [
            '"balanced quotes"',
            "(balanced parentheses)",
            '("complex" AND balanced)',
            'multiple "quotes" and (parentheses)',
            "((nested) parentheses)",
        ]

        for query in valid_balanced_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                is_valid
            ), f"Query '{query}' should be valid but got error: {error_msg}"

    def test_edge_cases(self):
        """Test edge cases and special scenarios."""
        # Empty and whitespace queries
        invalid_empty_queries = [
            "",
            "   ",
            "\t",
            "\n",
        ]

        for query in invalid_empty_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                not is_valid
            ), f"Empty/whitespace query '{repr(query)}' should be invalid"
            assert "cannot be empty" in error_msg

        # Non-string inputs
        non_string_inputs = [None, 123, [], {}, True]
        for invalid_input in non_string_inputs:
            is_valid, error_msg = self.validator.validate_query(invalid_input)
            assert (
                not is_valid
            ), f"Non-string input {type(invalid_input)} should be invalid"
            assert "must be a string" in error_msg


class TestNewscatcherApiValidation:
    """Test cases for the validate_query method in the main client."""

    def setup_method(self):
        """Set up test fixtures."""
        self.client = NewscatcherApi(api_key="test_key")

    def test_validate_query_method_exists(self):
        """Test that the validate_query method exists on the client."""
        assert hasattr(self.client, "validate_query")
        assert callable(self.client.validate_query)

    def test_validate_query_basic_functionality(self):
        """Test basic functionality of client.validate_query method."""
        # Valid query
        is_valid, error_msg = self.client.validate_query("valid query")
        assert is_valid
        assert error_msg == ""

        # Invalid query
        is_valid, error_msg = self.client.validate_query("invalid [query]")
        assert not is_valid
        assert "must not include following characters" in error_msg

    def test_validate_query_return_format(self):
        """Test that validate_query returns the correct format."""
        is_valid, error_msg = self.client.validate_query("test query")

        # Check return types
        assert isinstance(is_valid, bool)
        assert isinstance(error_msg, str)

        # For valid query, error message should be empty
        assert error_msg == ""

    def test_get_all_articles_with_validation_enabled(self):
        """Test that get_all_articles validates queries when validation is enabled."""
        # Mock the search.post method
        with patch.object(self.client, "search") as mock_search:
            mock_response = Mock()
            mock_response.articles = []
            mock_response.total_pages = 1
            mock_search.post.return_value = mock_response

            # Valid query should not raise an exception
            try:
                articles = self.client.get_all_articles(
                    q="valid query", validate_query=True, from_="1d"
                )
                # Should succeed (though will be empty due to mock)
            except ValueError:
                pytest.fail("Valid query should not raise ValueError")

            # Invalid query should raise ValueError
            with pytest.raises(ValueError, match="Invalid query syntax"):
                self.client.get_all_articles(
                    q="invalid [query]", validate_query=True, from_="1d"
                )

    def test_get_all_articles_with_validation_disabled(self):
        """Test that get_all_articles skips validation when disabled."""
        # Mock the search.post method
        with patch.object(self.client, "search") as mock_search:
            mock_response = Mock()
            mock_response.articles = []
            mock_response.total_pages = 1
            mock_search.post.return_value = mock_response

            # Invalid query should NOT raise exception when validation is disabled
            try:
                articles = self.client.get_all_articles(
                    q="invalid [query]", validate_query=False, from_="1d"
                )
                # Should succeed even with invalid query
            except ValueError:
                pytest.fail(
                    "Invalid query should not raise ValueError when validation is disabled"
                )

    def test_validation_consistency_with_server(self):
        """
        Test that validation results are consistent with expected server behavior.

        This test verifies that queries that would fail on the server
        are caught by local validation.
        """
        # These queries should all fail validation and would fail on server
        server_failing_queries = [
            "query[with]brackets",  # Forbidden characters
            "*wildcard",  # Invalid wildcard placement
            "AND starting",  # Starts with operator
            "ending AND ",  # Ends with operator
            "double OR OR operators",  # Invalid operator combination
            'unbalanced "quote',  # Unbalanced quotes
            "unbalanced (paren",  # Unbalanced parentheses
        ]

        for query in server_failing_queries:
            is_valid, error_msg = self.client.validate_query(query)
            assert not is_valid, (
                f"Query '{query}' should fail validation to match server behavior. "
                f"This query would fail on the server."
            )
            assert (
                error_msg
            ), f"Error message should be provided for invalid query '{query}'"

    def test_real_world_queries(self):
        """Test with real-world query examples that should be valid."""
        real_world_queries = [
            "artificial intelligence",
            "climate change AND renewable energy",
            '"machine learning" OR "deep learning"',
            "(python OR javascript) AND programming",
            "startup* AND (funding OR investment)",
            "COVID-19 OR coronavirus",
            '"breaking news" AND (politics OR election)',
            "stock market AND (Tesla OR Apple OR Google)",
            "(fintech OR cryptocurrency) AND regulation",
            "renewable energy NOT nuclear",
            "AI safety AND ethics",
        ]

        for query in real_world_queries:
            is_valid, error_msg = self.client.validate_query(query)
            assert (
                is_valid
            ), f"Real-world query '{query}' should be valid but got error: {error_msg}"


class TestAsyncNewscatcherApiValidation:
    """Test cases for the validate_query method in the async client."""

    def setup_method(self):
        """Set up test fixtures."""
        self.client = AsyncNewscatcherApi(api_key="test_key")

    def test_validate_query_method_exists(self):
        """Test that the validate_query method exists on the async client."""
        assert hasattr(self.client, "validate_query")
        assert callable(self.client.validate_query)

    def test_validate_query_basic_functionality(self):
        """Test basic functionality of async client.validate_query method."""
        # Valid query
        is_valid, error_msg = self.client.validate_query("valid query")
        assert is_valid
        assert error_msg == ""

        # Invalid query
        is_valid, error_msg = self.client.validate_query("invalid [query]")
        assert not is_valid
        assert "must not include following characters" in error_msg

    @pytest.mark.asyncio
    async def test_get_all_articles_with_validation_enabled(self):
        """Test that async get_all_articles validates queries when validation is enabled."""
        # Mock the search.post method
        with patch.object(self.client, "search") as mock_search:
            mock_response = Mock()
            mock_response.articles = []
            mock_response.total_pages = 1
            mock_search.post.return_value = mock_response

            # Valid query should not raise an exception
            try:
                articles = await self.client.get_all_articles(
                    q="valid query", validate_query=True, from_="1d"
                )
                # Should succeed (though will be empty due to mock)
            except ValueError:
                pytest.fail("Valid query should not raise ValueError")

            # Invalid query should raise ValueError
            with pytest.raises(ValueError, match="Invalid query syntax"):
                await self.client.get_all_articles(
                    q="invalid [query]", validate_query=True, from_="1d"
                )


class TestValidationErrorMessages:
    """Test that error messages match the original API validation messages."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_forbidden_character_error_format(self):
        """Test that forbidden character errors match API format."""
        is_valid, error_msg = self.validator.validate_query("test[query]")
        assert not is_valid
        assert "Query parameter must not include following characters" in error_msg
        assert "Please remove them from query parameter" in error_msg

    def test_asterisk_error_format(self):
        """Test that asterisk errors match API format."""
        is_valid, error_msg = self.validator.validate_query("*invalid")
        assert not is_valid
        assert (
            "The wildcard (*) character in query parameter must be preceded"
            in error_msg
        )
        assert (
            "by at least one alphabet or number. Please modify the query." in error_msg
        )

    def test_operator_start_error_format(self):
        """Test that operator start errors match API format."""
        is_valid, error_msg = self.validator.validate_query("AND query")
        assert not is_valid
        assert "Query parameter starts with an operator" in error_msg
        assert (
            "The query must not start with such operator. Please remove it."
            in error_msg
        )

    def test_operator_end_error_format(self):
        """Test that operator end errors match API format."""
        is_valid, error_msg = self.validator.validate_query("query AND ")
        assert not is_valid
        assert "Query parameter ends with an operator" in error_msg
        assert "Please remove an unused operator." in error_msg

    def test_operator_combination_error_format(self):
        """Test that operator combination errors match API format."""
        is_valid, error_msg = self.validator.validate_query("query OR OR term")
        assert not is_valid
        assert "Query parameter contains operator" in error_msg
        assert "used without keywords" in error_msg
        assert "Please add keywords or remove one of the operators" in error_msg

    def test_unbalanced_quotes_error_format(self):
        """Test that unbalanced quote errors match API format."""
        is_valid, error_msg = self.validator.validate_query('query "unbalanced')
        assert not is_valid
        assert "Query parameter contains an unclosed quote" in error_msg
        assert "Please close the quote before proceeding." in error_msg

    def test_unbalanced_parentheses_error_format(self):
        """Test that unbalanced parentheses errors match API format."""
        is_valid, error_msg = self.validator.validate_query("query (unbalanced")
        assert not is_valid
        assert "Query parameter contains an unclosed round bracket" in error_msg
        assert "Please close the bracket before proceeding." in error_msg


class TestBulkValidation:
    """Test bulk validation scenarios for performance and correctness."""

    def setup_method(self):
        """Set up test fixtures."""
        self.client = NewscatcherApi(api_key="test_key")

    def test_bulk_validation_performance(self):
        """Test validation performance with multiple queries."""
        queries = [
            "query 1",
            "query 2 AND term",
            '"exact phrase"',
            "wildcard*",
            "(grouped terms)",
            "invalid [query]",  # This one should fail
            "another valid query",
            "AND invalid start",  # This should fail
            "valid complex (query AND term) OR other*",
            'unbalanced "quote',  # This should fail
        ]

        results = []
        for query in queries:
            is_valid, error_msg = self.client.validate_query(query)
            results.append((query, is_valid, error_msg))

        # Should have processed all queries
        assert len(results) == len(queries)

        # Check specific results
        valid_results = [r for r in results if r[1]]
        invalid_results = [r for r in results if not r[1]]

        # Should have both valid and invalid results
        assert len(valid_results) >= 6, "Should have at least 6 valid queries"
        assert len(invalid_results) >= 3, "Should have at least 3 invalid queries"

        # Check specific invalid queries
        invalid_queries = {r[0]: r[2] for r in invalid_results}
        assert "invalid [query]" in invalid_queries
        assert "AND invalid start" in invalid_queries
        assert 'unbalanced "quote' in invalid_queries

    def test_validation_with_llm_generated_queries(self):
        """Test validation with typical LLM-generated query patterns."""
        llm_queries = [
            "artificial intelligence trends 2024",
            "machine learning AND python programming",
            "blockchain OR cryptocurrency market analysis",
            '"natural language processing" AND applications',
            "(deep learning OR neural networks) AND research",
            "climate change AND (renewable energy OR sustainability)",
            "startup funding AND (venture capital OR angel investment)",
            "cybersecurity AND (data privacy OR encryption)",
        ]

        # All these should be valid
        for query in llm_queries:
            is_valid, error_msg = self.client.validate_query(query)
            assert (
                is_valid
            ), f"LLM-style query '{query}' should be valid but got error: {error_msg}"


class TestValidationRules:
    """Test specific validation rules to ensure they match the original elasticsearch_helper.py logic."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_special_asterisk_cases(self):
        """Test special asterisk cases from the original logic."""
        # Single asterisk should be valid (special case in original code)
        is_valid, error_msg = self.validator.validate_query("*")
        assert is_valid, f"Single asterisk should be valid, got error: {error_msg}"

        # Multiple asterisks without other characters should be invalid
        is_valid, error_msg = self.validator.validate_query("***")
        assert not is_valid, "Multiple asterisks should be invalid"

    def test_url_encoded_operators(self):
        """Test URL-encoded operators and characters."""
        # URL-encoded forbidden characters
        url_encoded_tests = [
            ("%5B", False),  # [
            ("%5D", False),  # ]
            ("%2F", False),  # /
            ("%5C", False),  # \
            ("%3A", False),  # :
            ("%5E", False),  # ^
        ]

        for char, should_be_valid in url_encoded_tests:
            query = f"query{char}test"
            is_valid, error_msg = self.validator.validate_query(query)
            assert (
                is_valid == should_be_valid
            ), f"Query '{query}' validation result should be {should_be_valid}"

    def test_complex_operator_scenarios(self):
        """ """
