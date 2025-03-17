"""
Newscatcher SDK environment configuration.

This module provides utilities for loading API credentials and configuration
settings from environment variables or .env files.
"""

import os
import logging
from typing import Dict, Any, Optional
from pathlib import Path

# Setup logging
logger = logging.getLogger(__name__)

# Default values
DEFAULT_TIMEOUT = 60
DEFAULT_MAX_ARTICLES = 50000


def load_env_file(env_path: Optional[str] = None) -> None:
    """
    Load environment variables from .env file if available.

    This function will attempt to load dotenv if installed,
    but will not fail if the package is not available.

    Args:
        env_path: Optional path to .env file
    """
    try:
        from dotenv import load_dotenv  # type: ignore

        if env_path and os.path.exists(env_path):
            load_dotenv(env_path)
            logger.info(f"Loaded environment from {env_path}")
        else:
            # Try to find .env file in the current directory or parent directories
            for path in [".env", "../.env", "../../.env"]:
                if os.path.exists(path):
                    load_dotenv(path)
                    logger.info(f"Loaded environment from {path}")
                    break
            else:
                logger.warning("No .env file found, using system environment variables")
    except ImportError:
        logger.warning(
            "python-dotenv package not installed, using system environment variables. "
            "Install with 'pip install python-dotenv' to use .env files."
        )


def get_config() -> Dict[str, Any]:
    """
    Get configuration from environment variables.

    Returns:
        Dictionary of configuration values
    """
    # Try to load from .env file first
    load_env_file()

    # Get API key (required)
    api_key = os.environ.get("NEWSCATCHER_API_KEY")

    # Get optional configurations
    timeout = os.environ.get("NEWSCATCHER_TIMEOUT")
    max_articles = os.environ.get("NEWSCATCHER_MAX_ARTICLES")

    # Get test configurations
    test_mode = os.environ.get("TEST_MODE", "mock")  # Default to mock mode
    test_data_dir = os.environ.get("TEST_DATA_DIR", "./tests/data")

    # Create configuration dictionary
    config = {
        "api_key": api_key,
        "timeout": int(timeout) if timeout else DEFAULT_TIMEOUT,
        "max_articles": int(max_articles) if max_articles else DEFAULT_MAX_ARTICLES,
        "test": {"mode": test_mode, "data_dir": test_data_dir},
    }

    # Validate required configurations
    if not api_key:
        logger.warning(
            "No API key found in environment variables. "
            "Set NEWSCATCHER_API_KEY environment variable or use a .env file."
        )

    return config


def ensure_data_dir(config: Dict[str, Any]) -> None:
    """
    Ensure the test data directory exists.

    Args:
        config: Configuration dictionary from get_config()
    """
    data_dir = Path(config["test"]["data_dir"])

    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created test data directory: {data_dir}")


def add_gitignore_entry() -> None:
    """
    Add test data directory to .gitignore if not already present.
    """
    gitignore_path = Path(".gitignore")
    test_data_entry = "tests/data/"

    # Create .gitignore if it doesn't exist
    if not gitignore_path.exists():
        with open(gitignore_path, "w") as f:
            f.write(f"# Newscatcher test data\n{test_data_entry}\n")
        logger.info("Created .gitignore with test data entry")
        return

    # Check if entry already exists
    with open(gitignore_path, "r") as f:
        content = f.read()

    if test_data_entry not in content:
        with open(gitignore_path, "a") as f:
            f.write(f"\n# Newscatcher test data\n{test_data_entry}\n")
        logger.info("Added test data entry to .gitignore")
