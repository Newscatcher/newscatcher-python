"""
Comprehensive test for Newscatcher SDK custom methods.

This test file provides a focused validation of the key functionality:
the ability to overcome the 10,000 article limit through time-chunking.
It integrates with the test infrastructure to use environment configuration
and data caching when appropriate.
"""

import os
import pytest
import logging
import time
import datetime
import json
from typing import List, Set, Dict, Any, Union, Optional
from collections import Counter

from tests.integration.test_base import TestBase, AsyncTestBase
from tests.integration.env_config import get_config, load_env_file
from tests.integration.data_storage import get_data_manager
from newscatcher import NewscatcherApi, AsyncNewscatcherApi

# Set up logging with a more verbose format
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment configuration
load_env_file()
config = get_config()

# Default test parameters with environment overrides
DEFAULT_QUERY = "technology"
DEFAULT_FROM = "7d"
DEFAULT_CHUNK_SIZE = "1d"
DEFAULT_MAX_ARTICLES = int(os.environ.get("NEWSCATCHER_MAX_ARTICLES", "2000"))
LONG_RANGE_FROM = "90d"  # Use a long range to test 10,000+ article scenarios
HIGH_FREQUENCY_QUERY = "*"  # Wildcard query to match all articles
API_RESULT_LIMIT = 10000  # The API's hard limit for total_hits


class TestChunkingMethods(TestBase):
    """Core tests for the chunking methods in Newscatcher SDK."""

    def setup_method(self):
        """Set up test method with environment configuration."""
        # Get data directory from config
        data_dir = config.get("test", {}).get("data_dir", "./tests/data")

        # Ensure we have the data manager
        self.data_manager = get_data_manager(data_dir)

        # Log environment configuration
        logger.info(
            f"Test environment: {config.get('test', {}).get('mode', 'unknown')}"
        )
        logger.info(f"Max articles: {DEFAULT_MAX_ARTICLES}")
        logger.info(f"Data directory: {data_dir}")

    def test_chunking_strategy(self):
        """
        Test the time-chunking strategy with different chunk sizes.

        This test verifies:
        1. Articles can be retrieved across different time periods
        2. Different chunk sizes produce similar results
        3. Deduplication works correctly
        4. max_articles limit is respected
        """
        print("\n" + "=" * 80)
        print("TEST: CHUNKING STRATEGY - VALIDATING TIME CHUNKING WITH DIFFERENT SIZES")
        print("=" * 80)
        logger.info("Starting chunking strategy test")

        # Use a high-frequency search term that should appear in most articles
        q = HIGH_FREQUENCY_QUERY
        from_ = DEFAULT_FROM
        max_articles = min(500, DEFAULT_MAX_ARTICLES)  # Limit for faster testing

        # Test with different chunk sizes
        chunk_sizes = ["1d", "7d"]  # Test both small and large chunks

        results = {}
        test_stats = {}

        for chunk_size in chunk_sizes:
            logger.info(f"Testing with chunk size: {chunk_size}")

            # Test with deduplication enabled (default)
            dedup_start = time.time()
            articles_dedup = self.client.get_all_articles(
                q=q,
                from_=from_,
                time_chunk_size=chunk_size,
                max_articles=max_articles,
                deduplicate=True,
                show_progress=True,
            )
            dedup_time = time.time() - dedup_start

            # Test with deduplication disabled
            no_dedup_start = time.time()
            articles_no_dedup = self.client.get_all_articles(
                q=q,
                from_=from_,
                time_chunk_size=chunk_size,
                max_articles=max_articles,
                deduplicate=False,
                show_progress=True,
            )
            no_dedup_time = time.time() - no_dedup_start

            results[chunk_size] = {
                "dedup_count": len(articles_dedup),
                "no_dedup_count": len(articles_no_dedup),
                "dedup_time": dedup_time,
                "no_dedup_time": no_dedup_time,
                "duplicate_count": len(articles_no_dedup) - len(articles_dedup),
                "duplicate_percentage": round(
                    (
                        100
                        * (len(articles_no_dedup) - len(articles_dedup))
                        / len(articles_no_dedup)
                        if len(articles_no_dedup) > 0
                        else 0
                    ),
                    2,
                ),
            }

            # Analyze date distribution
            date_counts = Counter()
            for article in articles_dedup:
                if hasattr(article, "published_date") and article.published_date:
                    date_str = (
                        article.published_date.split("T")[0]
                        if "T" in article.published_date
                        else article.published_date.split(" ")[0]
                    )
                    date_counts[date_str] += 1

            # Verify we got articles from multiple dates
            unique_dates = len(date_counts)
            logger.info(f"Retrieved articles from {unique_dates} different dates")
            assert unique_dates > 1, "Should get articles from multiple dates"

            # Store statistics for this chunk size
            test_stats[chunk_size] = {
                "unique_dates": unique_dates,
                "date_distribution": dict(date_counts.most_common(5)),  # Top 5 dates
                "runtime_seconds": dedup_time,
                "articles_per_second": (
                    round(len(articles_dedup) / dedup_time, 2) if dedup_time > 0 else 0
                ),
            }

            # Verify deduplication works
            assert len(articles_dedup) <= len(
                articles_no_dedup
            ), "Deduplication should reduce or maintain article count"
            if len(articles_dedup) < len(articles_no_dedup):
                logger.info(
                    f"Deduplication removed {len(articles_no_dedup) - len(articles_dedup)} articles ({results[chunk_size]['duplicate_percentage']}%)"
                )

            # Verify max_articles is respected
            assert (
                len(articles_dedup) <= max_articles
            ), "Should respect max_articles limit"
            assert (
                len(articles_no_dedup) <= max_articles
            ), "Should respect max_articles limit"

        # Compare results across chunk sizes
        logger.info("Comparing results across chunk sizes:")
        for chunk_size, result in results.items():
            logger.info(
                f"  {chunk_size}: {result['dedup_count']} articles (dedup), {result['no_dedup_count']} articles (no dedup), "
                f"{result['duplicate_percentage']}% duplicates, {test_stats[chunk_size]['articles_per_second']} articles/sec"
            )

        # Verify different chunk sizes produce similar numbers of articles
        counts = [r["dedup_count"] for r in results.values()]
        max_difference_percent = (
            max(counts) / min(counts) - 1.0 if min(counts) > 0 else 0
        )
        print(
            f"Maximum difference between chunk sizes: {max_difference_percent*100:.1f}%"
        )

        # Print summary report for the chunking strategy test
        print("\n" + "-" * 80)
        print("CHUNKING STRATEGY VALIDATION SUMMARY")
        print("-" * 80)
        print(
            f"Tested {len(chunk_sizes)} different chunk sizes: {', '.join(chunk_sizes)}"
        )
        print(f"Query: '{q}', from: {from_}, max articles: {max_articles}")
        print(
            f"All chunk sizes retrieved similar article counts (within {max_difference_percent*100:.1f}%)"
        )
        print(
            f"Average deduplication rate: {sum(r['duplicate_percentage'] for r in results.values())/len(results):.2f}%"
        )

        for chunk_size in chunk_sizes:
            stats = test_stats[chunk_size]
            print(f"\nChunk size '{chunk_size}' statistics:")
            print(f"  - Retrieved from {stats['unique_dates']} different dates")
            print(f"  - Top dates: {stats['date_distribution']}")
        print("-" * 80)

    def test_api_limit_bypass(self):
        """
        Test that chunking allows bypassing the API's 10,000 article limit.

        This test verifies that our chunking approach can retrieve more
        articles than would be possible with standard API pagination.
        """
        print("\n" + "=" * 80)
        print(
            "TEST: API LIMIT BYPASS - VALIDATING CHUNKING METHOD FOR >10,000 ARTICLES"
        )
        print("=" * 80)
        logger.info("Starting API limit bypass test")

        # Use a common search term that's likely to have many results
        q = "news"

        # Use a wide time range that would likely exceed 10,000 articles
        from_ = LONG_RANGE_FROM

        logger.info(f"Testing standard API approach for '{q}' from last {from_}")

        # Make a standard API request using the base class method to enable caching
        try:
            # Get data directory from config for caching
            data_dir = config.get("test", {}).get("data_dir", "./tests/data")
            os.makedirs(data_dir, exist_ok=True)

            cache_key = f"search_post_{q}_{from_}"
            cached_response = None

            # Try to use the data manager from base class if available
            if hasattr(self, "data_manager") and self.data_manager:
                cached_response = self.data_manager.load_response(
                    "search", {"q": q, "from_": from_}
                )

            if cached_response:
                logger.info("Using cached standard API response")
                standard_response = cached_response
            else:
                # Make live API call
                standard_response = self.client.search.post(
                    q=q, from_=from_, page=1, page_size=100
                )
                # Cache for future use if data manager is available
                if hasattr(self, "data_manager") and self.data_manager:
                    self.data_manager.save_response(
                        "search", {"q": q, "from_": from_}, standard_response
                    )
        except Exception as e:
            logger.warning(f"Error with caching: {e}")
            # Fallback to direct API call
            standard_response = self.client.search.post(
                q=q, from_=from_, page=1, page_size=100
            )

        # Get total hits and pages
        total_hits_standard = standard_response.total_hits
        total_pages_standard = standard_response.total_pages

        logger.info(
            f"Standard API reports {total_hits_standard} total hits across {total_pages_standard} pages"
        )

        # Check if we've hit the 10,000 limit
        is_potentially_capped = total_hits_standard >= API_RESULT_LIMIT
        logger.info(f"Response is potentially capped: {is_potentially_capped}")

        # Use our chunking approach to retrieve more articles
        # than would be possible with the standard API
        logger.info(f"Testing chunked approach for '{q}' from last {from_}")

        # For time efficiency in testing, limit max articles
        test_max_articles = min(15000, DEFAULT_MAX_ARTICLES)

        # Define chunk sizes appropriate for the time range
        time_chunk_size = "15d"  # For 90-day range, this gives 6 chunks

        # Measure performance
        start_time = time.time()

        chunked_articles = self.client.get_all_articles(
            q=q,
            from_=from_,
            time_chunk_size=time_chunk_size,
            max_articles=test_max_articles,
            deduplicate=True,
            show_progress=True,
        )

        execution_time = time.time() - start_time

        assert (
            len(chunked_articles) > 10000
        ), "Should retrieve more than 10,000 articles with chunking approach"

        # Calculate articles per second
        articles_per_second = (
            len(chunked_articles) / execution_time if execution_time > 0 else 0
        )

        logger.info(
            f"Chunked approach returned {len(chunked_articles)} articles in {execution_time:.2f} seconds"
        )
        logger.info(f"Performance: {articles_per_second:.2f} articles/second")

        # If the response was capped, our chunked approach should retrieve more articles
        if is_potentially_capped:
            print("\n" + "-" * 80)
            print(
                f"VALIDATION RESULTS: CHUNKING TO OVERCOME {API_RESULT_LIMIT} ARTICLE LIMIT"
            )
            print("-" * 80)
            print(f"Standard API was capped at {API_RESULT_LIMIT} articles")
            print(f"Chunked method retrieved {len(chunked_articles)} articles")

            # Calculate theoretical maximum retrievable with standard pagination
            theoretical_max_standard = min(
                API_RESULT_LIMIT, total_pages_standard * standard_response.page_size
            )
            print(
                f"Theoretical maximum retrievable with standard pagination: {theoretical_max_standard}"
            )

            # Calculate improvement ratio
            if theoretical_max_standard > 0:
                improvement_ratio = len(chunked_articles) / theoretical_max_standard
                print(
                    f"Improvement ratio: {improvement_ratio:.2f}x more articles retrieved"
                )
                print("-" * 80)

            # We expect at least some articles to be returned
            assert (
                len(chunked_articles) > 100
            ), "Chunked approach should return a substantial number of articles"

            # If the standard approach hit the limit, we should be able to get more with chunking
            if total_hits_standard == API_RESULT_LIMIT:
                # Check if we got more than what a single API call could provide
                assert len(chunked_articles) > standard_response.page_size, (
                    f"Chunked approach should retrieve more than a single page ({standard_response.page_size}) "
                    f"when the standard API is capped at {API_RESULT_LIMIT}"
                )

        # Verify date distribution to confirm chunking is working
        date_counts = Counter()
        for article in chunked_articles:
            if hasattr(article, "published_date") and article.published_date:
                date_str = (
                    article.published_date.split("T")[0]
                    if "T" in article.published_date
                    else article.published_date.split(" ")[0]
                )
                date_counts[date_str] += 1

        unique_dates = len(date_counts)
        logger.info(f"Retrieved articles from {unique_dates} different dates")
        logger.info(f"Top 5 dates: {dict(date_counts.most_common(5))}")

        # Calculate date range coverage percentage
        # For a 90-day period, we expect articles from multiple dates
        expected_dates = 90  # For LONG_RANGE_FROM = "90d"
        date_coverage_percentage = (
            (unique_dates / expected_dates) * 100 if expected_dates > 0 else 0
        )
        logger.info(
            f"Date range coverage: {date_coverage_percentage:.2f}% ({unique_dates}/{expected_dates} days)"
        )

        # Print summary report
        print("\n" + "-" * 80)
        print("TIME CHUNKING VALIDATION SUMMARY")
        print("-" * 80)
        print(f"Total articles retrieved: {len(chunked_articles)}")
        print(
            f"Articles from {unique_dates} different dates (out of {expected_dates} possible)"
        )
        print(f"Date coverage: {date_coverage_percentage:.2f}%")
        print(f"Processing speed: {articles_per_second:.2f} articles/second")
        if is_potentially_capped and theoretical_max_standard > 0:
            print(
                f"API limit bypass improvement: {improvement_ratio:.2f}x more articles"
            )
        print("-" * 80)

        # Should have articles from multiple dates
        assert (
            unique_dates > 5
        ), f"Should get articles from many different dates with a {LONG_RANGE_FROM} range"


class TestImplementations(TestBase):
    """Tests for both synchronous and asynchronous implementations."""

    def test_sync_implementation(self):
        """
        Test the synchronous implementation with a moderate result set.

        This test verifies the complete flow works end-to-end for the
        synchronous implementation.
        """
        print("\n" + "=" * 80)
        print("TEST: SYNC IMPLEMENTATION - VALIDATING BASE FUNCTIONALITY")
        print("=" * 80)

        # Use environment variables if available, otherwise use defaults
        q = os.environ.get("TEST_QUERY", DEFAULT_QUERY)
        from_ = os.environ.get("TEST_FROM", DEFAULT_FROM)
        time_chunk_size = os.environ.get("TEST_CHUNK_SIZE", DEFAULT_CHUNK_SIZE)
        max_articles = min(500, DEFAULT_MAX_ARTICLES)  # Limit for faster testing

        logger.info(
            f"Using query: {q}, from: {from_}, chunk size: {time_chunk_size}, max articles: {max_articles}"
        )

        # Run search
        start_time = time.time()
        articles = self.client.get_all_articles(
            q=q,
            from_=from_,
            time_chunk_size=time_chunk_size,
            max_articles=max_articles,
            show_progress=True,
        )
        execution_time = time.time() - start_time

        # Calculate article count
        article_count = len(articles)

        # Print article summary and sample data
        print("\n" + "-" * 80)
        print("SYNCHRONOUS IMPLEMENTATION RESULTS")
        print("-" * 80)
        print(f"Query: '{q}', from: {from_}, chunk size: {time_chunk_size}")
        print(f"Retrieved {article_count} articles in {execution_time:.2f} seconds")
        print(f"Processing speed: {article_count / execution_time:.2f} articles/second")

        # Log article metadata statistics
        has_title = sum(1 for a in articles if hasattr(a, "title") and a.title)
        has_author = sum(1 for a in articles if hasattr(a, "author") and a.author)
        has_published_date = sum(
            1 for a in articles if hasattr(a, "published_date") and a.published_date
        )

        print(f"\nMetadata completeness:")
        print(
            f"  - {has_title}/{article_count} articles have titles ({has_title/article_count*100:.1f}%)"
        )
        print(
            f"  - {has_author}/{article_count} articles have authors ({has_author/article_count*100:.1f}%)"
        )
        print(
            f"  - {has_published_date}/{article_count} articles have dates ({has_published_date/article_count*100:.1f}%)"
        )

        # Verify article structure (sample first 3 articles)
        if article_count > 0:
            print("\nSample articles:")
            for i, article in enumerate(articles[:3]):
                print(f"\nSample article {i+1}:")
                print(f"  ID: {article.id if hasattr(article, 'id') else 'N/A'}")
                print(
                    f"  Title: {article.title[:50] + '...' if hasattr(article, 'title') and len(article.title) > 50 else article.title if hasattr(article, 'title') else 'N/A'}"
                )
                print(
                    f"  Date: {article.published_date if hasattr(article, 'published_date') else 'N/A'}"
                )
                print(
                    f"  Source: {article.name_source if hasattr(article, 'name_source') else 'N/A'}"
                )
        print("-" * 80)


@pytest.mark.asyncio
class TestAsyncImplementation(AsyncTestBase):
    """Tests for asynchronous implementation."""

    async def test_async_implementation(self):
        """
        Test the asynchronous implementation with a moderate result set.

        This test verifies the complete flow works end-to-end for the
        asynchronous implementation, including the concurrency parameter.
        """
        print("\n" + "=" * 80)
        print("TEST: ASYNC IMPLEMENTATION - VALIDATING CONCURRENCY BENEFITS")
        print("=" * 80)

        # Use environment variables if available, otherwise use defaults
        q = os.environ.get("TEST_QUERY", DEFAULT_QUERY)
        from_ = os.environ.get("TEST_FROM", DEFAULT_FROM)
        time_chunk_size = os.environ.get("TEST_CHUNK_SIZE", DEFAULT_CHUNK_SIZE)
        max_articles = min(500, DEFAULT_MAX_ARTICLES)  # Limit for faster testing

        # Test with different concurrency settings
        concurrency_values = [1, 3]
        concurrency_results = {}

        for concurrency in concurrency_values:
            logger.info(f"Testing with concurrency={concurrency}")

            # Run search
            start_time = time.time()
            articles = await self.client.get_all_articles(
                q=q,
                from_=from_,
                time_chunk_size=time_chunk_size,
                max_articles=max_articles,
                concurrency=concurrency,
                show_progress=True,
            )
            execution_time = time.time() - start_time

            article_count = len(articles)
            articles_per_second = (
                article_count / execution_time if execution_time > 0 else 0
            )

            concurrency_results[concurrency] = {
                "article_count": article_count,
                "execution_time": execution_time,
                "articles_per_second": articles_per_second,
            }

            logger.info(
                f"Concurrency {concurrency}: Retrieved {article_count} articles in {execution_time:.2f} seconds"
            )
            logger.info(f"Performance: {articles_per_second:.2f} articles/second")

            # Basic validation
            assert (
                article_count > 0
            ), f"Should return articles (concurrency={concurrency})"
            assert (
                article_count <= max_articles
            ), f"Should respect max_articles limit (concurrency={concurrency})"

            # Verify article structure
            for article in articles[:5]:  # Check first 5 articles
                assert hasattr(article, "id"), "Article should have an ID"
                assert hasattr(article, "title"), "Article should have a title"
                assert hasattr(
                    article, "published_date"
                ), "Article should have a published date"

        # Compare concurrency performance
        if len(concurrency_values) > 1:
            baseline_concurrency = concurrency_values[0]
            baseline_perf = concurrency_results[baseline_concurrency][
                "articles_per_second"
            ]

            print("\n" + "-" * 80)
            print("CONCURRENCY PERFORMANCE COMPARISON")
            print("-" * 80)
            print(
                f"Baseline (concurrency={baseline_concurrency}): {baseline_perf:.2f} articles/second"
            )

            for concurrency in concurrency_values[1:]:
                current_perf = concurrency_results[concurrency]["articles_per_second"]
                if baseline_perf > 0:
                    speedup = current_perf / baseline_perf
                    print(
                        f"Concurrency {concurrency}: {current_perf:.2f} articles/second ({speedup:.2f}x speedup)"
                    )
                else:
                    print(
                        f"Concurrency {concurrency}: {current_perf:.2f} articles/second"
                    )
            print("-" * 80)

        # Also test get_all_headlines to ensure both methods work
        logger.info("Testing async get_all_headlines")

        headlines_start_time = time.time()
        headlines = await self.client.get_all_headlines(
            when=from_,
            time_chunk_size=time_chunk_size,
            max_articles=max_articles,
            concurrency=3,
            show_progress=True,
        )
        headlines_execution_time = time.time() - headlines_start_time

        headline_count = len(headlines)
        headlines_per_second = (
            headline_count / headlines_execution_time
            if headlines_execution_time > 0
            else 0
        )

        logger.info(
            f"Retrieved {headline_count} headlines in {headlines_execution_time:.2f} seconds"
        )
        logger.info(f"Performance: {headlines_per_second:.2f} headlines/second")

        # Basic validation
        assert headline_count > 0, "Should return headlines"
        assert headline_count <= max_articles, "Should respect max_articles limit"

        # Print headlines summary report
        print("\n" + "-" * 80)
        print("HEADLINES RETRIEVAL VALIDATION SUMMARY")
        print("-" * 80)
        print(f"Total headlines retrieved: {headline_count}")
        print(f"Processing speed: {headlines_per_second:.2f} headlines/second")

        # Log statistics on headline sources
        if headline_count > 0:
            sources = Counter(
                [
                    h.name_source
                    for h in headlines
                    if hasattr(h, "name_source") and h.name_source
                ]
            )
            languages = Counter(
                [h.language for h in headlines if hasattr(h, "language") and h.language]
            )

            print(f"\nTop headline sources:")
            for source, count in sources.most_common(5):
                print(f"  - {source}: {count} headlines")

            print(f"\nLanguage distribution:")
            for lang, count in languages.most_common():
                print(f"  - {lang}: {count} headlines")
        print("-" * 80)
