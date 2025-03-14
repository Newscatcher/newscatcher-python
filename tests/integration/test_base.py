"""
Integration tests for Newscatcher SDK.

This module provides the base setup for running integration tests
with real API calls and caching of responses.
"""

import os
import sys
import pytest
import logging
from typing import Dict, Any, Optional
import os.path

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Import required modules
try:
    from dotenv import load_dotenv

    # Try to load from .env file in various locations
    env_paths = [".env", "../.env", "../../.env"]
    for path in env_paths:
        if os.path.exists(path):
            logger.info(f"Loading environment from {path}")
            load_dotenv(path)
            break
    else:
        logger.warning("No .env file found, using system environment variables")
except ImportError:
    logger.warning(
        "python-dotenv package not installed, using system environment variables"
    )

# Import the data manager
from tests.integration.data_storage import DataManager

# Import the Newscatcher client
from newscatcher import NewscatcherApi, AsyncNewscatcherApi


class TestBase:
    """Base class for Newscatcher integration tests."""

    @classmethod
    def setup_class(cls):
        """Set up the test environment."""
        # Get API key from environment
        cls.api_key = os.environ.get("NEWSCATCHER_API_KEY")
        logger.info(f"API key available: {bool(cls.api_key)}")

        # Get timeout from environment or use default
        timeout = os.environ.get("NEWSCATCHER_TIMEOUT")
        cls.timeout = int(timeout) if timeout else 60

        # Get test mode from environment or use default
        cls.test_mode = os.environ.get("TEST_MODE", "mock")

        # Get test data directory from environment or use default
        cls.test_data_dir = os.environ.get("TEST_DATA_DIR", "./tests/data")

        # Ensure test data directory exists
        os.makedirs(cls.test_data_dir, exist_ok=True)

        # Initialize data manager
        cls.data_manager = DataManager(cls.test_data_dir)

        # Initialize client if API key is available
        if cls.api_key:
            cls.client = NewscatcherApi(api_key=cls.api_key, timeout=cls.timeout)
        else:
            logger.warning("No API key found - tests will be skipped")

    def run_test_with_cache(
        self,
        endpoint: str,
        method_name: str,
        params: Dict[str, Any],
        use_cache: bool = True,
    ) -> Dict[str, Any]:
        """
        Run a test with caching support.

        This method will check for cached responses first if use_cache is True
        and the test mode is not 'live'. If no cache is available or test mode
        is 'live', it will make a real API call and cache the response.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            method_name: Name of the method to call (post, get, etc.)
            params: Parameters to pass to the method
            use_cache: Whether to use cached responses

        Returns:
            API response
        """
        # Check if we should use cached responses
        if use_cache and self.test_mode != "live":
            cached_response = self.data_manager.load_response(endpoint, params)
            if cached_response:
                logger.info(f"Using cached response for {endpoint}")
                return cached_response

        # No cache or live mode, make a real API call
        if not hasattr(self, "client"):
            pytest.skip("No API key available for live tests")

        # Get the method to call
        method = getattr(getattr(self.client, endpoint), method_name)

        # Make the API call
        logger.info(f"Making live API call to {endpoint}")
        response = method(**params)

        # Cache the response if test mode is cache
        if self.test_mode == "cache" or use_cache:
            self.data_manager.save_response(endpoint, params, response)

        return response


class AsyncTestBase:
    """Base class for asynchronous Newscatcher integration tests."""

    @classmethod
    def setup_class(cls):
        """Set up the test environment."""
        # Get API key from environment
        cls.api_key = os.environ.get("NEWSCATCHER_API_KEY")
        logger.info(f"API key available for async tests: {bool(cls.api_key)}")

        # Get timeout from environment or use default
        timeout = os.environ.get("NEWSCATCHER_TIMEOUT")
        cls.timeout = int(timeout) if timeout else 60

        # Get test mode from environment or use default
        cls.test_mode = os.environ.get("TEST_MODE", "mock")

        # Get test data directory from environment or use default
        cls.test_data_dir = os.environ.get("TEST_DATA_DIR", "./tests/data")

        # Ensure test data directory exists
        os.makedirs(cls.test_data_dir, exist_ok=True)

        # Initialize data manager
        cls.data_manager = DataManager(cls.test_data_dir)

        # Initialize async client if API key is available
        if cls.api_key:
            cls.client = AsyncNewscatcherApi(api_key=cls.api_key, timeout=cls.timeout)
        else:
            logger.warning("No API key found for async tests - tests will be skipped")

    async def run_test_with_cache(
        self,
        endpoint: str,
        method_name: str,
        params: Dict[str, Any],
        use_cache: bool = True,
    ) -> Dict[str, Any]:
        """
        Run an async test with caching support.

        This method will check for cached responses first if use_cache is True
        and the test mode is not 'live'. If no cache is available or test mode
        is 'live', it will make a real API call and cache the response.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            method_name: Name of the method to call (post, get, etc.)
            params: Parameters to pass to the method
            use_cache: Whether to use cached responses

        Returns:
            API response
        """
        # Check if we should use cached responses
        if use_cache and self.test_mode != "live":
            cached_response = self.data_manager.load_response(endpoint, params)
            if cached_response:
                logger.info(f"Using cached response for {endpoint}")
                return cached_response

        # No cache or live mode, make a real API call
        if not hasattr(self, "client"):
            pytest.skip("No API key available for live tests")

        # Get the method to call
        method = getattr(getattr(self.client, endpoint), method_name)

        # Make the API call
        logger.info(f"Making live API call to {endpoint}")
        response = await method(**params)

        # Cache the response if test mode is cache
        if self.test_mode == "cache" or use_cache:
            self.data_manager.save_response(endpoint, params, response)

        return response
