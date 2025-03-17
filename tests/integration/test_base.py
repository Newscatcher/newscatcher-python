"""
Integration tests for Newscatcher SDK.

This module provides the base setup for running integration tests
with real API calls and caching of responses.
"""

import os
import sys
import json
import pytest
import logging
from typing import Dict, Any, Optional, Union, ClassVar, Type

from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Import required modules
try:
    from dotenv import load_dotenv  # type: ignore

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

    # Declare class variables with type annotations
    api_key: ClassVar[Optional[str]]
    timeout: ClassVar[int]
    test_mode: ClassVar[str]
    test_data_dir: ClassVar[str]
    data_manager: ClassVar[DataManager]
    client: ClassVar[Optional[NewscatcherApi]]

    @classmethod
    def setup_class(cls) -> None:
        """Set up the test environment."""
        # Get API key from environment
        cls.api_key = os.environ.get("NEWSCATCHER_API_KEY")
        logger.info(f"API key available: {bool(cls.api_key)}")

        # Get timeout from environment or use default
        timeout = os.environ.get("NEWSCATCHER_TIMEOUT")
        cls.timeout = int(timeout) if timeout else 60

        # Get test mode from environment or use default
        cls.test_mode = os.environ.get("TEST_MODE", "mock")
        logger.info(f"Test mode: {cls.test_mode}")

        # Get test data directory from environment or use default
        cls.test_data_dir = os.environ.get("TEST_DATA_DIR", "./tests/data")

        # Ensure test data directory exists
        os.makedirs(cls.test_data_dir, exist_ok=True)

        # Initialize data manager
        cls.data_manager = DataManager(cls.test_data_dir)

        # Initialize client
        if cls.api_key:
            cls.client = NewscatcherApi(api_key=cls.api_key, timeout=cls.timeout)
        elif cls.test_mode == "mock":
            # Use a dummy key in mock mode
            logger.info("Using dummy API key in mock mode")
            cls.client = NewscatcherApi(
                api_key="dummy_key_for_mocks", timeout=cls.timeout
            )
        else:
            logger.warning("No API key found - tests will be skipped")
            cls.client = None

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

        # If we're in mock mode and no cache, try to use mock data
        if self.test_mode == "mock":
            # See if we have a mock for this endpoint
            mock_dir = Path("tests/mocks")
            mock_path = mock_dir / f"{endpoint}.json"

            if mock_path.exists():
                with open(mock_path, "r") as f:
                    logger.info(f"Using mock data for {endpoint}")
                    return json.load(f)
            else:
                # Create mocks directory if it doesn't exist
                os.makedirs(mock_dir, exist_ok=True)

                # Create a simple mock response
                mock_response = {
                    "status": "ok",
                    "total_hits": 100,
                    "total_pages": 2,
                    "page": 1,
                    "page_size": 50,
                    "articles": [
                        {
                            "id": f"mock1_{endpoint}",
                            "title": f"Mock {endpoint.title()} 1",
                            "published_date": "2025-03-15T12:00:00Z",
                        },
                        {
                            "id": f"mock2_{endpoint}",
                            "title": f"Mock {endpoint.title()} 2",
                            "published_date": "2025-03-16T12:00:00Z",
                        },
                    ],
                }

                # Save the mock response for future use
                with open(mock_path, "w") as f:
                    json.dump(mock_response, f)

                logger.info(f"Created and using new mock data for {endpoint}")
                return mock_response

        # No cache or mock, make a real API call
        if (
            not hasattr(self, "client")
            or self.client is None
            or (self.test_mode != "mock" and not self.api_key)
        ):
            pytest.skip("No API key available for live tests")

        try:
            # Get the method to call
            if self.client is not None:
                endpoint_obj = getattr(self.client, endpoint, None)
                if endpoint_obj is not None:
                    method = getattr(endpoint_obj, method_name, None)
                    if method is not None:
                        # Make the API call
                        logger.info(f"Making live API call to {endpoint}")
                        response = method(**params)

                        # Cache the response if test mode is cache
                        if self.test_mode == "cache" or use_cache:
                            self.data_manager.save_response(endpoint, params, response)

                        return response
                    else:
                        raise AttributeError(
                            f"Method {method_name} not found on {endpoint}"
                        )
                else:
                    raise AttributeError(f"Endpoint {endpoint} not found on client")
            else:
                pytest.skip("Client is not initialized")

            # This return is to satisfy the type checker
            return {}

        except Exception as e:
            logger.error(f"Error making API call to {endpoint}: {str(e)}")
            if self.test_mode == "mock":
                # Create a simple mock response in case of error
                return {
                    "status": "ok",
                    "total_hits": 10,
                    "total_pages": 1,
                    "page": 1,
                    "page_size": 10,
                    "articles": [
                        {
                            "id": "mock_fallback",
                            "title": "Mock Fallback",
                            "published_date": "2025-03-17T12:00:00Z",
                        }
                    ],
                }
            else:
                raise


class AsyncTestBase:
    """Base class for asynchronous Newscatcher integration tests."""

    # Declare class variables with type annotations
    api_key: ClassVar[Optional[str]]
    timeout: ClassVar[int]
    test_mode: ClassVar[str]
    test_data_dir: ClassVar[str]
    data_manager: ClassVar[DataManager]
    client: ClassVar[Optional[AsyncNewscatcherApi]]

    @classmethod
    def setup_class(cls) -> None:
        """Set up the test environment."""
        # Get API key from environment
        cls.api_key = os.environ.get("NEWSCATCHER_API_KEY")
        logger.info(f"API key available for async tests: {bool(cls.api_key)}")

        # Get timeout from environment or use default
        timeout = os.environ.get("NEWSCATCHER_TIMEOUT")
        cls.timeout = int(timeout) if timeout else 60

        # Get test mode from environment or use default
        cls.test_mode = os.environ.get("TEST_MODE", "mock")
        logger.info(f"Async test mode: {cls.test_mode}")

        # Get test data directory from environment or use default
        cls.test_data_dir = os.environ.get("TEST_DATA_DIR", "./tests/data")

        # Ensure test data directory exists
        os.makedirs(cls.test_data_dir, exist_ok=True)

        # Initialize data manager
        cls.data_manager = DataManager(cls.test_data_dir)

        # Initialize async client
        if cls.api_key:
            cls.client = AsyncNewscatcherApi(api_key=cls.api_key, timeout=cls.timeout)
        elif cls.test_mode == "mock":
            # Use a dummy key in mock mode
            logger.info("Using dummy API key in mock mode for async tests")
            cls.client = AsyncNewscatcherApi(
                api_key="dummy_key_for_mocks", timeout=cls.timeout
            )
        else:
            logger.warning("No API key found for async tests - tests will be skipped")
            cls.client = None

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

        # If we're in mock mode and no cache, try to use mock data
        if self.test_mode == "mock":
            # See if we have a mock for this endpoint
            mock_dir = Path("tests/mocks")
            mock_path = mock_dir / f"{endpoint}.json"

            if mock_path.exists():
                with open(mock_path, "r") as f:
                    logger.info(f"Using mock data for {endpoint}")
                    return json.load(f)
            else:
                # Create mocks directory if it doesn't exist
                os.makedirs(mock_dir, exist_ok=True)

                # Create a simple mock response
                mock_response = {
                    "status": "ok",
                    "total_hits": 100,
                    "total_pages": 2,
                    "page": 1,
                    "page_size": 50,
                    "articles": [
                        {
                            "id": f"mock1_async_{endpoint}",
                            "title": f"Mock Async {endpoint.title()} 1",
                            "published_date": "2025-03-15T12:00:00Z",
                        },
                        {
                            "id": f"mock2_async_{endpoint}",
                            "title": f"Mock Async {endpoint.title()} 2",
                            "published_date": "2025-03-16T12:00:00Z",
                        },
                    ],
                }

                # Save the mock response for future use
                with open(mock_path, "w") as f:
                    json.dump(mock_response, f)

                logger.info(f"Created and using new mock data for async {endpoint}")
                return mock_response

        # No cache or mock, make a real API call
        if (
            not hasattr(self, "client")
            or self.client is None
            or (self.test_mode != "mock" and not self.api_key)
        ):
            pytest.skip("No API key available for async live tests")

        try:
            # Get the method to call
            if self.client is not None:
                endpoint_obj = getattr(self.client, endpoint, None)
                if endpoint_obj is not None:
                    method = getattr(endpoint_obj, method_name, None)
                    if method is not None:
                        # Make the API call
                        logger.info(f"Making async live API call to {endpoint}")
                        response = await method(**params)

                        # Cache the response if test mode is cache
                        if self.test_mode == "cache" or use_cache:
                            self.data_manager.save_response(endpoint, params, response)

                        return response
                    else:
                        raise AttributeError(
                            f"Method {method_name} not found on {endpoint}"
                        )
                else:
                    raise AttributeError(f"Endpoint {endpoint} not found on client")
            else:
                pytest.skip("Async client is not initialized")

            # This return is to satisfy the type checker
            return {}

        except Exception as e:
            logger.error(f"Error making async API call to {endpoint}: {str(e)}")
            if self.test_mode == "mock":
                # Create a simple mock response in case of error
                return {
                    "status": "ok",
                    "total_hits": 10,
                    "total_pages": 1,
                    "page": 1,
                    "page_size": 10,
                    "articles": [
                        {
                            "id": "mock_async_fallback",
                            "title": "Mock Async Fallback",
                            "published_date": "2025-03-17T12:00:00Z",
                        }
                    ],
                }
            else:
                raise
