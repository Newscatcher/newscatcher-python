"""
Test data storage utility for Newscatcher SDK.

This module provides utilities for saving and loading API responses for testing.
It supports caching responses to reduce API calls during development and testing.
"""

import os
import json
import hashlib
import datetime
from pathlib import Path
from typing import Dict, Any, Optional, Union

# Type aliases
ResponseData = Dict[str, Any]


class DataManager:
    """
    Manager for test data storage and retrieval.

    This class handles saving and loading API responses for testing purposes,
    enabling caching of responses to reduce API calls during development.
    """

    def __init__(self, data_dir: str = "./tests/data"):
        """
        Initialize the DataManager.

        Args:
            data_dir: Directory to store cached API responses
        """
        self.data_dir = Path(data_dir)
        self.mock_dir = Path("tests/mocks")

        # Create the data directory if it doesn't exist
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True, exist_ok=True)

        # Create the mocks directory if it doesn't exist
        if not self.mock_dir.exists():
            self.mock_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories for different endpoints
        for endpoint in ["search", "latestheadlines", "other"]:
            endpoint_dir = self.data_dir / endpoint
            if not endpoint_dir.exists():
                endpoint_dir.mkdir(exist_ok=True)

    def _generate_cache_key(self, endpoint: str, params: Dict[str, Any]) -> str:
        """
        Generate a unique cache key for the request parameters.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            params: Request parameters

        Returns:
            A unique cache key for the parameters
        """
        # Create a string representation of the parameters
        param_str = json.dumps(params, sort_keys=True)

        # Generate a hash of the parameters
        param_hash = hashlib.md5(param_str.encode()).hexdigest()

        return param_hash

    def get_cache_path(self, endpoint: str, params: Dict[str, Any]) -> Path:
        """
        Get the cache file path for the request parameters.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            params: Request parameters

        Returns:
            Path to the cache file
        """
        cache_key = self._generate_cache_key(endpoint, params)

        # Use a subdirectory for the endpoint
        if endpoint in ["search", "latestheadlines"]:
            endpoint_dir = self.data_dir / endpoint
        else:
            endpoint_dir = self.data_dir / "other"

        return endpoint_dir / f"{cache_key}.json"

    def save_response(
        self,
        endpoint: str,
        params: Dict[str, Any],
        response: ResponseData,
        expiry_days: int = 7,
    ) -> Path:
        """
        Save an API response to the cache.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            params: Request parameters
            response: API response data
            expiry_days: Number of days until the cache expires

        Returns:
            Path to the saved cache file
        """
        cache_path = self.get_cache_path(endpoint, params)

        # Convert response to a serializable format if it's not already
        serializable_response = response
        if not isinstance(response, dict) and not isinstance(response, list):
            # Try to convert object to dict using various methods
            try:
                # Method 1: Try __dict__ attribute if available
                if hasattr(response, "__dict__"):
                    serializable_response = {**response.__dict__}
                # Method 2: Try to_dict method if available
                elif hasattr(response, "to_dict") and callable(
                    getattr(response, "to_dict")
                ):
                    serializable_response = response.to_dict()
                # Method 3: Extract public attributes
                else:
                    serializable_response = {}
                    for attr in dir(response):
                        if not attr.startswith("_") and not callable(
                            getattr(response, attr)
                        ):
                            try:
                                value = getattr(response, attr)
                                # Check if the value is JSON serializable
                                json.dumps({attr: value})
                                serializable_response[attr] = value
                            except (TypeError, OverflowError):
                                # Skip attributes that can't be serialized
                                serializable_response[attr] = str(value)
            except Exception as e:
                # Fallback to string representation if all else fails
                serializable_response = {
                    "error": f"Could not serialize response: {str(e)}",
                    "response_type": str(type(response)),
                    "string_representation": str(response),
                }

        # Add metadata to the cached response
        cache_data = {
            "metadata": {
                "endpoint": endpoint,
                "params": params,
                "cached_at": datetime.datetime.now().isoformat(),
                "expires_at": (
                    datetime.datetime.now() + datetime.timedelta(days=expiry_days)
                ).isoformat(),
            },
            "response": serializable_response,
        }

        # Save to file
        try:
            with open(cache_path, "w") as f:
                json.dump(cache_data, f, indent=2)
        except (TypeError, OverflowError) as e:
            # If we still can't serialize, save a simplified version
            simplified_cache_data = {
                "metadata": cache_data["metadata"],
                "response": {
                    "error": f"Failed to serialize response: {str(e)}",
                    "response_type": str(type(response)),
                },
            }
            with open(cache_path, "w") as f:
                json.dump(simplified_cache_data, f, indent=2)

        return cache_path

    def load_response(
        self, endpoint: str, params: Dict[str, Any], ignore_expiry: bool = False
    ) -> Optional[ResponseData]:
        """
        Load an API response from the cache.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            params: Request parameters
            ignore_expiry: Whether to ignore the cache expiry date

        Returns:
            Cached API response or None if not found or expired
        """
        cache_path = self.get_cache_path(endpoint, params)

        # Check if cache file exists
        if not cache_path.exists():
            # Try to load from mock data as fallback
            mock_path = self.mock_dir / f"{endpoint}.json"
            if mock_path.exists():
                with open(mock_path, "r") as f:
                    mock_data = json.load(f)
                    return mock_data
            return None

        # Load from file
        with open(cache_path, "r") as f:
            cache_data = json.load(f)

        # Check if cache is expired
        if not ignore_expiry:
            expires_at = datetime.datetime.fromisoformat(
                cache_data["metadata"]["expires_at"]
            )
            if datetime.datetime.now() > expires_at:
                return None

        return cache_data["response"]

    def save_mock_response(self, endpoint: str, response: ResponseData) -> Path:
        """
        Save a mock response for an endpoint.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)
            response: Mock response data

        Returns:
            Path to the saved mock file
        """
        mock_path = self.mock_dir / f"{endpoint}.json"

        # Save to file
        with open(mock_path, "w") as f:
            json.dump(response, f, indent=2)

        return mock_path

    def load_mock_response(self, endpoint: str) -> Optional[ResponseData]:
        """
        Load a mock response for an endpoint.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)

        Returns:
            Mock response or None if not found
        """
        mock_path = self.mock_dir / f"{endpoint}.json"

        # Check if mock file exists
        if not mock_path.exists():
            return None

        # Load from file
        with open(mock_path, "r") as f:
            return json.load(f)

    def generate_mock_response(self, endpoint: str) -> ResponseData:
        """
        Generate a mock response for an endpoint.

        Args:
            endpoint: API endpoint (search, latestheadlines, etc.)

        Returns:
            Generated mock response
        """
        # Create a simple mock response based on the endpoint
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
                    "summary": f"This is a mock summary for {endpoint} 1",
                    "published_date": "2025-03-15T12:00:00Z",
                    "link": f"https://example.com/{endpoint}/1",
                    "language": "en",
                    "author": "Mock Author",
                    "authors": ["Mock Author"],
                    "score": 0.95,
                },
                {
                    "id": f"mock2_{endpoint}",
                    "title": f"Mock {endpoint.title()} 2",
                    "summary": f"This is a mock summary for {endpoint} 2",
                    "published_date": "2025-03-16T12:00:00Z",
                    "link": f"https://example.com/{endpoint}/2",
                    "language": "en",
                    "author": "Mock Author 2",
                    "authors": ["Mock Author 2"],
                    "score": 0.92,
                },
            ],
        }

        # Save the mock response for future use
        self.save_mock_response(endpoint, mock_response)

        return mock_response

    def clear_cache(self, endpoint: Optional[str] = None) -> int:
        """
        Clear the cache for a specific endpoint or all endpoints.

        Args:
            endpoint: Optional endpoint to clear cache for,
                     if None, clears all cache

        Returns:
            Number of cache files removed
        """
        count = 0

        if endpoint:
            # Clear cache for specific endpoint
            if endpoint in ["search", "latestheadlines"]:
                endpoint_dir = self.data_dir / endpoint
            else:
                endpoint_dir = self.data_dir / "other"

            if endpoint_dir.exists():
                for cache_file in endpoint_dir.glob("*.json"):
                    cache_file.unlink()
                    count += 1
        else:
            # Clear all cache
            for endpoint_dir in self.data_dir.glob("*"):
                if endpoint_dir.is_dir():
                    for cache_file in endpoint_dir.glob("*.json"):
                        cache_file.unlink()
                        count += 1

        return count

    def clear_mocks(self) -> int:
        """
        Clear all mock responses.

        Returns:
            Number of mock files removed
        """
        count = 0

        if self.mock_dir.exists():
            for mock_file in self.mock_dir.glob("*.json"):
                mock_file.unlink()
                count += 1

        return count

    def get_all_responses(
        self, endpoint: Optional[str] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Get all cached responses for a specific endpoint or all endpoints.

        Args:
            endpoint: Optional endpoint to get responses for,
                    if None, gets all responses

        Returns:
            Dictionary of cache keys to cached responses
        """
        responses = {}

        if endpoint:
            # Get responses for specific endpoint
            if endpoint in ["search", "latestheadlines"]:
                endpoint_dir = self.data_dir / endpoint
            else:
                endpoint_dir = self.data_dir / "other"

            if endpoint_dir.exists():
                for cache_file in endpoint_dir.glob("*.json"):
                    with open(cache_file, "r") as f:
                        responses[cache_file.stem] = json.load(f)
        else:
            # Get all responses
            for endpoint_dir in self.data_dir.glob("*"):
                if endpoint_dir.is_dir():
                    for cache_file in endpoint_dir.glob("*.json"):
                        with open(cache_file, "r") as f:
                            responses[cache_file.stem] = json.load(f)

        return responses


# Convenience function to get a data manager instance
def get_data_manager(data_dir: Optional[str] = None) -> DataManager:
    """
    Get a DataManager instance.

    Args:
        data_dir: Optional directory to store cached API responses

    Returns:
        DataManager instance
    """
    if data_dir:
        return DataManager(data_dir)

    # Try to get directory from environment
    data_dir = os.environ.get("TEST_DATA_DIR", "./tests/data")
    return DataManager(data_dir)
