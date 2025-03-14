"""
Utility functions for the Newscatcher SDK.

This module contains utility functions for time parsing, chunk creation,
progress tracking, and formatting that are used by the Newscatcher client.
"""

import datetime
from typing import List, Tuple, Union, Iterator, Optional, Dict, Any, Set
from dateutil.parser import parse as parse_date
from dateutil.relativedelta import relativedelta


def parse_time_parameters(
    endpoint_type: str, **kwargs
) -> Tuple[datetime.datetime, datetime.datetime, datetime.timedelta]:
    """
    Parse time parameters based on the endpoint type.

    Args:
        endpoint_type: Either 'search' or 'latestheadlines'
        **kwargs: Parameters for the specific endpoint
            - For 'search': from_, to_, time_chunk_size
            - For 'latestheadlines': when, time_chunk_size

    Returns:
        Tuple of (from_date, to_date, chunk_delta)

    Raises:
        ValueError: If time parameters or chunk formats are invalid
    """
    now = datetime.datetime.now(datetime.timezone.utc)

    # Parse chunk size first (common to both endpoints)
    time_chunk_size = kwargs.get("time_chunk_size", "1h")  # Default to 1 hour chunks

    # Handle numeric values like "1d" or "12h"
    if (
        isinstance(time_chunk_size, str)
        and len(time_chunk_size) >= 2
        and time_chunk_size[-1].lower() in ["d", "h"]
        and time_chunk_size[:-1].isdigit()
    ):

        chunk_value = int(time_chunk_size[:-1])
        chunk_unit = time_chunk_size[-1].lower()

        if chunk_unit == "d":
            chunk_delta = datetime.timedelta(days=chunk_value)
        elif chunk_unit == "h":
            chunk_delta = datetime.timedelta(hours=chunk_value)
        else:
            raise ValueError(
                f"Unsupported time chunk unit: {chunk_unit}. Use 'd' for days or 'h' for hours."
            )
    else:
        raise ValueError(
            f"Invalid time_chunk_size format: {time_chunk_size}. Use format like '1d' or '12h'."
        )

    # Handle endpoint-specific parameters
    if endpoint_type == "search":
        # Handle 'to' parameter for search
        to = kwargs.get("to")
        if to is None:
            to_date = now
        elif isinstance(to, str):
            # Check if it's a relative time string like "7d", "3m", "2w"
            if len(to) >= 2 and to[-1].lower() in ["d", "w", "m"] and to[:-1].isdigit():
                value = int(to[:-1])
                unit = to[-1].lower()

                if unit == "d":
                    to_date = now - datetime.timedelta(days=value)
                elif unit == "w":
                    to_date = now - datetime.timedelta(weeks=value)
                elif unit == "m":
                    to_date = now - relativedelta(months=value)
            else:
                # Treat as ISO date string
                to_date = parse_date(to)
        else:
            to_date = to

        # Handle 'from_' parameter for search
        from_ = kwargs.get("from_")
        if from_ is None:
            # Default to 7 days ago if not specified (aligning with API defaults)
            from_date = to_date - datetime.timedelta(days=7)
        elif isinstance(from_, str):
            # Check if it's a relative time string like "7d", "3m", "2w"
            if (
                len(from_) >= 2
                and from_[-1].lower() in ["d", "w", "m"]
                and from_[:-1].isdigit()
            ):
                value = int(from_[:-1])
                unit = from_[-1].lower()

                if unit == "d":
                    from_date = to_date - datetime.timedelta(days=value)
                elif unit == "w":
                    from_date = to_date - datetime.timedelta(weeks=value)
                elif unit == "m":
                    from_date = to_date - relativedelta(months=value)
            else:
                # Treat as ISO date string
                from_date = parse_date(from_)
        else:
            from_date = from_

    elif endpoint_type == "latestheadlines":
        # Always set to_date to now for latest headlines
        to_date = now

        # Parse 'when' parameter to determine from_date
        when = kwargs.get("when")
        if when is None:
            # Default to 7 days ago if not specified (aligning with API defaults)
            from_date = to_date - datetime.timedelta(days=7)
        elif isinstance(when, str):
            # Check if it's a relative time string like "7d", "3m", "2w"
            if (
                len(when) >= 2
                and when[-1].lower() in ["d", "w", "m"]
                and when[:-1].isdigit()
            ):
                value = int(when[:-1])
                unit = when[-1].lower()

                if unit == "d":
                    from_date = to_date - datetime.timedelta(days=value)
                elif unit == "w":
                    from_date = to_date - datetime.timedelta(weeks=value)
                elif unit == "m":
                    from_date = to_date - relativedelta(months=value)
            else:
                # Treat as ISO date string
                from_date = parse_date(when)
        else:
            # Assume when is already a datetime object
            from_date = when
    else:
        raise ValueError(
            f"Unknown endpoint type: {endpoint_type}. Use 'search' or 'latestheadlines'."
        )

    return from_date, to_date, chunk_delta


def create_time_chunks(
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    chunk_delta: datetime.timedelta,
) -> List[Tuple[datetime.datetime, datetime.datetime]]:
    """
    Break a time period into manageable chunks.

    Args:
        from_date: Start datetime
        to_date: End datetime
        chunk_delta: Size of each chunk as timedelta

    Returns:
        List of (chunk_start, chunk_end) datetime pairs
    """
    chunks = []
    chunk_start = from_date

    while chunk_start < to_date:
        chunk_end = min(chunk_start + chunk_delta, to_date)
        chunks.append((chunk_start, chunk_end))
        chunk_start = chunk_end

    return chunks


def setup_progress_tracking(
    chunks: List[Tuple[datetime.datetime, datetime.datetime]],
    show_progress: bool,
    description: str = "Processing chunks",
    is_test: bool = False,  # New parameter to indicate if this is a test run
) -> Iterator[Tuple[datetime.datetime, datetime.datetime]]:
    """
    Set up progress tracking for processing chunks.

    Args:
        chunks: List of chunks to process
        show_progress: Whether to show progress indicators
        description: Description for the progress bar
        is_test: Whether this is being run in a test environment

    Returns:
        Iterator with progress tracking if requested
    """
    # Always show progress in test environments if not explicitly disabled
    if is_test and show_progress is not False:
        show_progress = True

    if not show_progress:
        return chunks

    total_chunks = len(chunks)

    try:
        # Try to use tqdm if available
        from tqdm import tqdm

        return tqdm(chunks, desc=description, total=total_chunks)
    except ImportError:
        # Fall back to simple terminal output
        print(f"{description}: {total_chunks} chunks")
        if total_chunks > 1:
            print(f"Processing chunk 1/{total_chunks}...", end="", flush=True)

        # Create a wrapper to provide progress updates
        def progress_wrapper():
            for i, chunk in enumerate(chunks):
                yield chunk
                # Update progress
                if i < total_chunks - 1:
                    print(
                        f"\rProcessing chunk {i+2}/{total_chunks}...",
                        end="",
                        flush=True,
                    )
            print("\rCompleted all chunks.                    ")

        return progress_wrapper()


def format_datetime(dt_obj: Optional[Union[datetime.datetime, str]]) -> Optional[str]:
    """
    Format a datetime object or ISO string for API requests.

    Args:
        dt_obj: A datetime object or ISO-formatted string

    Returns:
        ISO-formatted string or None if input is None
    """
    if dt_obj is None:
        return None
    return dt_obj.isoformat() if hasattr(dt_obj, "isoformat") else dt_obj


def calculate_when_param(
    to_date: datetime.datetime, chunk_start: datetime.datetime
) -> str:
    """
    Calculate the 'when' parameter for latestheadlines based on time difference.

    Args:
        to_date: Current time (usually now)
        chunk_start: The start time of the chunk

    Returns:
        A string like "3d" or "12h" representing the time difference
    """
    time_diff = to_date - chunk_start

    # Convert to days or hours based on the size
    if time_diff.total_seconds() >= 86400:  # 1 day in seconds
        when_value = max(1, time_diff.days)
        when_param = f"{when_value}d"
    else:
        when_value = max(1, int(time_diff.total_seconds() / 3600))  # hours
        when_param = f"{when_value}h"

    return when_param
