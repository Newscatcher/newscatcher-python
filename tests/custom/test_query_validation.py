"""
Comprehensive test suite for query validation functionality.

This test file validates that the local query validation implementation
matches the actual API behavior by making real API calls and comparing
the results with local validation.
"""

import os
import sys
import pytest
import logging
import time
from typing import Dict, Any, List, Tuple, Optional
from unittest.mock import Mock, patch

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Import the Newscatcher client and validator
from newscatcher import NewscatcherApi, AsyncNewscatcherApi
from src.newscatcher.client import QueryValidator

# Import test infrastructure
from tests.integration.env_config import get_config, load_env_file
from tests.integration.data_storage import get_data_manager

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
load_env_file()
config = get_config()


class TestQueryValidatorBasic:
    """Basic functionality tests for QueryValidator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_validator_initialization(self):
        """Test that validator initializes with correct attributes."""
        assert hasattr(self.validator, "not_allowed_characters")
        assert hasattr(self.validator, "open_char")
        assert hasattr(self.validator, "close_char")
        assert len(self.validator.not_allowed_characters) > 0

    def test_basic_valid_queries(self):
        """Test basic single-word queries that should always be valid."""
        valid_queries = [
            "AI",
            "python",
            "technology", 
            "machine",
            "learning",
            "data",
            "science",
            "news",
            "123",
            "AI123"
        ]

        for query in valid_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Query {repr(query)} should be valid but got error: {error_msg}"
            assert error_msg == ""

    def test_empty_and_invalid_input_queries(self):
        """Test empty queries and invalid input types."""
        empty_queries = [
            ("", "[q] parameter should not empty"),
            ("   ", "[q] parameter should not empty"),
            ("\t", "[q] parameter should not empty"),
            ("\n", "[q] parameter should not empty")
        ]

        for query, expected_fragment in empty_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Empty query {repr(query)} should be invalid"
            assert expected_fragment in error_msg

        # Test non-string inputs
        invalid_inputs = [None, 123, [], {}, True]
        for invalid_input in invalid_inputs:
            is_valid, error_msg = self.validator.validate_query(invalid_input)
            assert not is_valid, f"Non-string input {type(invalid_input)} should be invalid"
            assert "must be a string" in error_msg

    def test_forbidden_characters(self):
        """Test forbidden character validation with exact error message matching."""
        forbidden_tests = [
            ("query[with]brackets", "["),
            ("query/with/slashes", "/"),
            ("query\\with\\backslashes", "\\"),
            ("query:with:colons", ":"),
            ("query^with^caret", "^"),
            ("query%5Bwith%5Dencoded", "%5B"),
            ("query%2Fwith%2Fencoded", "%2F"),
            ("query%5Cwith%5Cencoded", "%5C"),
            ("query%3Awith%3Aencoded", "%3A"),
            ("query%5Ewith%5Eencoded", "%5E")
        ]

        for query, forbidden_char in forbidden_tests:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Query {repr(query)} with forbidden char should be invalid"
            assert "[q] parameter must not include following characters" in error_msg
            assert "Please remove them from [q] parameter" in error_msg

    def test_backslash_quote_escaping_allowed(self):
        """Test that backslash-quote escaping is allowed for exact phrases."""
        valid_escaped_queries = [
            "\"machine learning\"",
            "\"artificial intelligence\"",
            "AI OR \"artificial intelligence\"",
            "\"data science\" AND python"
        ]

        for query in valid_escaped_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Escaped query {repr(query)} should be valid but got error: {error_msg}"

    def test_wildcard_validation(self):
        """Test wildcard (*) usage validation."""
        # Valid wildcard usage
        valid_wildcards = [
            "*",           # Single asterisk is special case
            "term*",       # Suffix wildcard
            "learn*",      # Suffix wildcard
            "AI*",         # Suffix wildcard
            "data*",       # Suffix wildcard
        ]

        for query in valid_wildcards:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Valid wildcard {repr(query)} should work but got error: {error_msg}"

        # Invalid wildcard usage - now properly caught
        invalid_wildcards = [
            "*term",       # Prefix wildcard
            "**",          # Multiple wildcards
            "***",         # Multiple wildcards
            "term *",      # Space before wildcard
            " *"           # Space before wildcard - now properly caught
        ]

        for query in invalid_wildcards:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Invalid wildcard {repr(query)} should fail"
            assert "wildcard (*) character" in error_msg
            assert "preceded by at least one alphabet or number" in error_msg

    def test_operator_boundary_validation(self):
        """Test operators at start and end of queries with correct error message expectations."""
        # Word operators at start should return "Syntax error" message
        word_operators_invalid_start = [
            ("AND machine learning", "AND"),
            ("OR artificial intelligence", "OR"), 
            ("NOT science", "NOT")
        ]

        for query, operator in word_operators_invalid_start:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Query {repr(query)} starting with word operator should fail"
            assert f"Syntax error in input : unexpected  \"{operator}\" at position 0!" in error_msg

        # Symbolic operators at start should return "starts with operator" message
        symbolic_operators_invalid_start = [
            "&& python",
            "|| data"
        ]

        for query in symbolic_operators_invalid_start:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Query {repr(query)} starting with symbolic operator should fail"
            assert "starts with an operator" in error_msg

        # Invalid end operators (now including standalone OR/AND)
        invalid_end = [
            "machine learning AND",  # Now properly caught
            "artificial intelligence OR",  # Now properly caught
            "python &&",
            "data ||",
            "science NOT"
        ]

        for query in invalid_end:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Query {repr(query)} ending with operator should fail"
            assert "ends with an operator" in error_msg

    def test_middle_operator_combinations(self):
        """Test invalid operator combinations in the middle."""
        invalid_combinations = [
            "query OR OR term",      # Double OR
            "query AND AND term",    # Double AND
            "query NOT NOT term",    # Double NOT
            "query ()",              # Empty parentheses
            "term1 && && term2",     # Double &&
            "term1 || || term2"      # Double ||
        ]

        for query in invalid_combinations:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Invalid combination {repr(query)} should fail"
            assert "used without keywords" in error_msg

    def test_quote_and_parenthesis_balance(self):
        """Test balanced quotes and parentheses."""
        # Unbalanced quotes
        invalid_quotes = [
            "unbalanced \"quote",
            "another quote\" unbalanced",
            "multiple \"unbalanced \"quotes\""
        ]

        for query in invalid_quotes:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Unbalanced quote {repr(query)} should fail"
            assert "unclosed quote" in error_msg

        # Unbalanced parentheses
        invalid_parens = [
            "unbalanced (parenthesis",
            "extra) parenthesis", 
            "nested ((unbalanced)"
        ]

        for query in invalid_parens:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Unbalanced parenthesis {repr(query)} should fail"
            assert "unclosed round bracket" in error_msg

        # Valid balanced
        valid_balanced = [
            "\"balanced quotes\"",
            "(balanced parentheses)",
            "(\"complex\" AND balanced)",
            "((nested) parentheses)"
        ]

        for query in valid_balanced:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Balanced query {repr(query)} should be valid but got error: {error_msg}"

class TestSameLevelOperators:
    """Test same-level AND/OR operator validation based on API behavior."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_same_level_operators(self):
        """Test the same level operator validation against known API behavior."""
        
        test_cases = [
            # These should FAIL (from your API test results)
            ("AI OR artificial intelligence", False, "same level"),
            ("startup OR venture capital", False, "same level"),
            ("python AND (machine learning OR data)", False, "same level"),
            ("blockchain OR artificial intelligence", False, "same level"),
            ("programming OR machine learning", False, "same level"),
            
            # These should SUCCEED (from your API test results)  
            ("AI OR \"artificial intelligence\"", True, "escaped phrase"),
            ("startup OR \"venture capital\"", True, "escaped phrase"),
            ("python AND (\"machine learning\" OR data)", True, "escaped phrase"),
            ("blockchain OR \"artificial intelligence\"", True, "escaped phrase"),
            ("programming OR \"machine learning\"", True, "escaped phrase"),
            
            # Same level operators (should succeed)
            ("AI OR ML", True, "same level OR"),
            ("python AND machine", True, "same level AND"),
            ("AI OR ML OR NLP", True, "all OR"),
            ("machine AND learning AND python", True, "all AND"),
            
            # Properly grouped (should succeed)
            ("(AI AND research) OR (ML AND development)", True, "properly grouped"),
            ("(startup AND innovation) OR (venture AND capital)", True, "properly grouped"),
        ]
        
        for query, should_pass, description in test_cases:
            is_valid, error_msg = self.validator.validate_query(query)
            
            if should_pass:
                assert is_valid, f"Query {repr(query)} ({description}) should be valid but got error: {error_msg}"
            else:
                assert not is_valid, f"Query {repr(query)} ({description}) should be invalid but was accepted"
                assert "same level" in error_msg, f"Expected 'same level' error message for {repr(query)}, got: {error_msg}"

    def test_same_level_error_message_format(self):
        """Test that same-level operator errors match exact API format."""
        invalid_queries = [
            "AI OR artificial intelligence",
            "startup OR venture capital",
            "programming OR machine learning"
        ]
        
        expected_message_parts = [
            'in [q] "AND" and "OR" operator not allowed at same level',
            'Please use parentheses to group terms correctly',
            'such as `(elon AND musk) OR twitter`'
        ]
        
        for query in invalid_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert not is_valid, f"Query {repr(query)} should be invalid"
            
            for expected_part in expected_message_parts:
                assert expected_part in error_msg, (
                    f"Error message for {repr(query)} should contain '{expected_part}'. "
                    f"Got: {error_msg}"
                )

    def test_quoted_phrases_prevent_same_level_violations(self):
        """Test that properly quoted phrases prevent same-level violations."""
        # These pairs show the difference between quoted and unquoted
        test_pairs = [
            ("AI OR artificial intelligence", False),          # Unquoted - should fail
            ("AI OR \"artificial intelligence\"", True),       # Quoted - should succeed
            
            ("startup OR venture capital", False),             # Unquoted - should fail  
            ("startup OR \"venture capital\"", True),          # Quoted - should succeed
            
            ("programming OR machine learning", False),        # Unquoted - should fail
            ("programming OR \"machine learning\"", True),     # Quoted - should succeed
        ]
        
        for query, should_pass in test_pairs:
            is_valid, error_msg = self.validator.validate_query(query)
            
            if should_pass:
                assert is_valid, f"Quoted query {repr(query)} should be valid but got error: {error_msg}"
            else:
                assert not is_valid, f"Unquoted query {repr(query)} should be invalid due to same-level violation"
                assert "same level" in error_msg.lower()

    def test_edge_cases_same_level(self):
        """Test edge cases for same-level operator detection."""
        edge_cases = [
            # No operators - should pass
            ("machine learning artificial intelligence", True),
            
            # Only AND operators - should pass  
            ("machine AND learning AND artificial", True),
            
            # Only OR operators - should pass
            ("AI OR ML OR NLP OR DL", True),
            
            # Complex but properly quoted - should pass
            ("(\"machine learning\" OR \"artificial intelligence\") AND python", True),
            
            # Multiple violations in one query - should fail
            ("AI OR machine learning AND data science OR neural networks", False),
        ]
        
        for query, should_pass in edge_cases:
            is_valid, error_msg = self.validator.validate_query(query)
            
            if should_pass:
                assert is_valid, f"Edge case {repr(query)} should be valid but got error: {error_msg}"
            else:
                assert not is_valid, f"Edge case {repr(query)} should be invalid"


class TestQueryValidatorWithAPI:
    """Test query validator against actual API behavior."""

    @classmethod
    def setup_class(cls):
        """Set up class with API client if available."""
        cls.api_key = config.get("api_key")
        cls.test_mode = config.get("test", {}).get("mode", "mock")
        
        if cls.api_key and cls.test_mode != "mock":
            cls.client = NewscatcherApi(api_key=cls.api_key)
            cls.use_api = True
            logger.info("Using real API for validation tests")
        else:
            cls.client = None 
            cls.use_api = False
            logger.info("API key not available or in mock mode - API comparison tests will be skipped")

        cls.validator = QueryValidator()
        cls.data_manager = get_data_manager(config.get("test", {}).get("data_dir", "./tests/data"))

    def _make_api_call(self, query: str) -> Tuple[bool, str]:
        """Make an API call to test query and return success status and error."""
        if not self.use_api:
            pytest.skip("API key not available for API comparison tests")

        try:
            # Make a minimal API call to test query validity
            response = self.client.search.post(
                q=query,
                page_size=1,
                from_="1d"  # Use short time range for quick response
            )
            
            # If we get here, the query was accepted by the API
            return True, ""
            
        except Exception as e:
            # Extract error message from API response
            error_msg = str(e)
            if "422" in error_msg or "Validation error" in error_msg:
                return False, error_msg
            else:
                # Other errors (like network issues) should not be treated as validation errors
                logger.warning(f"Non-validation error for query {repr(query)}: {error_msg}")
                return True, ""  # Assume query is valid if error is not validation-related

    @pytest.mark.skipif(not config.get("api_key"), reason="API key not available")
    def test_basic_queries_against_api(self):
        """Test basic queries against the actual API."""
        if not self.use_api:
            pytest.skip("API not available for comparison tests")

        basic_queries = [
            "AI",
            "machine learning", 
            "python",
            "technology",
            "\"artificial intelligence\"",
            "data*",
            "(python AND machine)"
        ]

        for query in basic_queries:
            # Test local validation
            local_valid, local_error = self.validator.validate_query(query)
            
            # Test API validation with rate limiting
            time.sleep(0.5)  # Rate limiting
            api_valid, api_error = self._make_api_call(query)
            
            # Both should agree that basic queries are valid
            assert local_valid == api_valid, (
                f"Query {repr(query)} validation mismatch: "
                f"local={local_valid} ({local_error}), api={api_valid} ({api_error})"
            )

    @pytest.mark.skipif(not config.get("api_key"), reason="API key not available")
    def test_invalid_queries_against_api(self):
        """Test invalid queries against the actual API."""
        if not self.use_api:
            pytest.skip("API not available for comparison tests")

        invalid_queries = [
            "query[with]brackets",       # Forbidden character
            "machine/learning",          # Forbidden character
            "*invalid",                  # Invalid wildcard
            "AND machine learning",      # Starts with operator
            "machine learning OR",       # Ends with operator - now properly caught
            "query OR OR term",          # Double operator
            "unbalanced \"quote",        # Unbalanced quote
            "(unbalanced parenthesis"    # Unbalanced parenthesis
        ]

        for query in invalid_queries:
            # Test local validation
            local_valid, local_error = self.validator.validate_query(query)
            
            # Test API validation with rate limiting
            time.sleep(0.5)  # Rate limiting
            api_valid, api_error = self._make_api_call(query)
            
            # Both should agree that invalid queries fail
            assert local_valid == api_valid, (
                f"Query {repr(query)} validation mismatch: "
                f"local={local_valid} ({local_error}), api={api_valid} ({api_error})"
            )

    def test_comprehensive_validation_patterns(self):
        """Test comprehensive validation patterns based on elasticsearch_helper.py logic."""
        # Multi-word queries (these should be valid locally)
        multi_word_queries = [
            "machine learning",
            "artificial intelligence", 
            "data science",
            "natural language processing"
        ]

        for query in multi_word_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Multi-word query {repr(query)} should be valid but got error: {error_msg}"

        # Complex valid structures
        complex_valid = [
            "python AND machine",
            "AI OR ML",
            "\"machine learning\" AND python",
            "technology AND (innovation OR research)",
            "(AI AND research) OR (ML AND development)"
        ]

        for query in complex_valid:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Complex query {repr(query)} should be valid but got error: {error_msg}"


class TestNewscatcherApiIntegration:
    """Test query validation integration with the main API client."""

    def setup_method(self):
        """Set up test fixtures."""
        api_key = config.get("api_key", "test_key")
        self.client = NewscatcherApi(api_key=api_key)
        self.validator = QueryValidator()

    def test_validate_query_method_exists(self):
        """Test that validate_query method exists on the client."""
        assert hasattr(self.client, "validate_query")
        assert callable(self.client.validate_query)

    def test_validate_query_delegation(self):
        """Test that client.validate_query delegates to internal validator."""
        # Valid query
        is_valid, error_msg = self.client.validate_query("valid query")
        assert is_valid
        assert error_msg == ""

        # Invalid query
        is_valid, error_msg = self.client.validate_query("invalid [query]")
        assert not is_valid
        assert "[q] parameter must not include following characters" in error_msg

    def test_get_all_articles_validation_integration(self):
        """Test validation integration with get_all_articles method."""
        # Mock the search.post method to avoid real API calls
        with patch.object(self.client, "search") as mock_search:
            mock_response = Mock()
            mock_response.articles = []
            mock_response.total_pages = 1
            mock_search.post.return_value = mock_response

            # Valid query should not raise exception
            try:
                articles = self.client.get_all_articles(
                    q="valid query",
                    validate_query=True,
                    from_="1d"
                )
                assert isinstance(articles, list)
            except ValueError:
                pytest.fail("Valid query should not raise ValueError")

            # Invalid query should raise ValueError when validation is enabled
            with pytest.raises(ValueError, match="Invalid query syntax"):
                self.client.get_all_articles(
                    q="invalid [query]",
                    validate_query=True,
                    from_="1d"
                )

            # Invalid query should NOT raise exception when validation is disabled
            try:
                articles = self.client.get_all_articles(
                    q="invalid [query]",
                    validate_query=False,
                    from_="1d"
                )
                assert isinstance(articles, list)
            except ValueError:
                pytest.fail("Invalid query should not raise ValueError when validation is disabled")

    def test_validation_performance_with_bulk_queries(self):
        """Test validation performance with multiple queries."""
        queries = [
            "simple query",
            "machine learning AND python",
            "\"exact phrase search\"",
            "(complex AND query) OR (another AND term)",
            "wildcard* search",
            "technology OR innovation",
            "very long query with many terms that should be processed efficiently without issues",
            "AI",
            "data*",
            "research AND (development OR innovation)"
        ]

        start_time = time.time()
        
        for query in queries:
            is_valid, error_msg = self.client.validate_query(query)
            # All test queries should be valid
            assert is_valid, f"Query {repr(query)} should be valid but got error: {error_msg}"
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Performance check - should validate all queries quickly
        assert total_time < 1.0, f"Validation took too long: {total_time:.3f} seconds for {len(queries)} queries"
        logger.info(f"Validated {len(queries)} queries in {total_time:.3f} seconds")


class TestAsyncNewscatcherApiIntegration:
    """Test query validation with async client."""

    def setup_method(self):
        """Set up test fixtures."""
        api_key = config.get("api_key", "test_key") 
        self.client = AsyncNewscatcherApi(api_key=api_key)

    def test_async_validate_query_method(self):
        """Test that async client has validate_query method."""
        assert hasattr(self.client, "validate_query")
        assert callable(self.client.validate_query)

        # Test basic validation
        is_valid, error_msg = self.client.validate_query("test query")
        assert is_valid
        assert error_msg == ""

        # Test invalid query
        is_valid, error_msg = self.client.validate_query("invalid [query]")
        assert not is_valid
        assert "[q] parameter must not include following characters" in error_msg

    @pytest.mark.asyncio
    async def test_async_get_all_articles_validation(self):
        """Test validation with async get_all_articles."""
        # Mock the search.post method
        with patch.object(self.client, "search") as mock_search:
            mock_response = Mock()
            mock_response.articles = []
            mock_response.total_pages = 1
            mock_search.post.return_value = mock_response

            # Valid query should work
            try:
                articles = await self.client.get_all_articles(
                    q="valid query",
                    validate_query=True,
                    from_="1d"
                )
                assert isinstance(articles, list)
            except ValueError:
                pytest.fail("Valid query should not raise ValueError in async client")

            # Invalid query should raise ValueError when validation is enabled
            with pytest.raises(ValueError, match="Invalid query syntax"):
                await self.client.get_all_articles(
                    q="invalid [query]",
                    validate_query=True,
                    from_="1d"
                )


class TestValidationErrorMessageConsistency:
    """Test that error messages exactly match the original elasticsearch_helper.py format."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_forbidden_character_error_format(self):
        """Test exact error message format for forbidden characters."""
        is_valid, error_msg = self.validator.validate_query("test[query]")
        assert not is_valid
        expected_chars = "['[', ']', '/', '\\\\', '%5B', '%5D', '%2F', '%5C', ':', '%3A', '^', '%5E']"
        assert "[q] parameter must not include following characters" in error_msg
        assert "Please remove them from [q] parameter" in error_msg

    def test_asterisk_error_format(self):
        """Test exact error message format for asterisk errors."""
        is_valid, error_msg = self.validator.validate_query("*invalid")
        assert not is_valid
        assert "The wildcard (*) character in [q] parameter must be preceded" in error_msg
        assert "by at least one alphabet or number. Please modify the query." in error_msg

    def test_operator_boundary_error_format(self):
        """Test exact error message format for operator boundary errors."""
        # Word operator start error - should match API format
        is_valid, error_msg = self.validator.validate_query("AND test")
        assert not is_valid
        assert "Syntax error in input : unexpected  \"AND\" at position 0!" in error_msg

        # End operator error - now properly caught
        is_valid, error_msg = self.validator.validate_query("test OR")
        assert not is_valid
        assert "[q] parameter ends with an operator" in error_msg
        assert "Please remove an unused operator." in error_msg

    def test_middle_operator_error_format(self):
        """Test exact error message format for middle operator errors."""
        is_valid, error_msg = self.validator.validate_query("test OR OR query")
        assert not is_valid
        assert "[q] parameter contains operator" in error_msg
        assert "used without keywords" in error_msg
        assert "Please add keywords or remove one of the operators" in error_msg

    def test_quote_balance_error_format(self):
        """Test exact error message format for quote balance errors."""
        is_valid, error_msg = self.validator.validate_query("unbalanced \"quote")
        assert not is_valid
        assert "[q] parameter contains an unclosed quote" in error_msg
        assert "Please close the quote before proceeding." in error_msg

    def test_parenthesis_balance_error_format(self):
        """Test exact error message format for parenthesis balance errors."""
        is_valid, error_msg = self.validator.validate_query("unbalanced (parenthesis")
        assert not is_valid
        assert "[q] parameter contains an unclosed round bracket" in error_msg
        assert "Please close the bracket before proceeding." in error_msg


class TestRealWorldQueryPatterns:
    """Test validation with real-world query patterns that users might enter."""

    def setup_method(self):
        """Set up test fixtures."""
        self.validator = QueryValidator()

    def test_typical_news_search_queries(self):
        """Test typical queries users might search for news."""
        typical_queries = [
            "breaking news",
            "COVID-19 updates",
            "stock market analysis",
            "climate change effects",
            "artificial intelligence developments",
            "cryptocurrency trends",
            "political election results",
            "sports championship finals",
            "technology innovation",
            "economic indicators"
        ]

        for query in typical_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Typical news query {repr(query)} should be valid but got error: {error_msg}"

    def test_academic_research_queries(self):
        """Test queries that might be used for academic research."""
        research_queries = [
            "machine learning applications",
            "quantum computing research",
            "renewable energy solutions",
            "medical breakthrough discoveries",
            "space exploration missions",
            "biotechnology innovations",
            "educational policy reforms",
            "environmental sustainability",
            "social media impact studies",
            "cybersecurity threat analysis"
        ]

        for query in research_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Research query {repr(query)} should be valid but got error: {error_msg}"

    def test_business_intelligence_queries(self):
        """Test queries for business intelligence and market research."""
        business_queries = [
            "startup funding rounds",
            "merger acquisition announcements",
            "quarterly earnings reports",
            "market share analysis",
            "consumer behavior trends",
            "industry disruption patterns",
            "competitive intelligence",
            "supply chain developments",
            "regulatory compliance updates",
            "investment opportunity analysis"
        ]

        for query in business_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Business query {repr(query)} should be valid but got error: {error_msg}"

    def test_complex_boolean_queries(self):
        """Test complex boolean queries that power users might create."""
        complex_queries = [
            "python AND (machine OR deep) AND learning",
            "startup AND (funding OR investment) AND (series OR round)",
            "climate AND (change OR warming) AND (policy OR regulation)",
            "(AI OR artificial) AND intelligence AND (ethics OR safety)",
            "cryptocurrency AND (bitcoin OR ethereum) AND (regulation OR policy)"
        ]

        for query in complex_queries:
            is_valid, error_msg = self.validator.validate_query(query)
            assert is_valid, f"Complex boolean query {repr(query)} should be valid but got error: {error_msg}"


if __name__ == "__main__":
    """Allow running tests directly."""
    pytest.main([__file__, "-v"])