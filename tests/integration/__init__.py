"""
Integration tests for the Newscatcher SDK.

This package contains tests that make real API calls to verify
the functionality of the Newscatcher SDK custom methods.
"""

# Import test utilities
from tests.integration.env_config import get_config, load_env_file
from tests.integration.data_storage import DataManager, get_data_manager
from tests.integration.test_base import TestBase, AsyncTestBase
