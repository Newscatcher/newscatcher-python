"""
Custom tests for Newscatcher SDK client.

This file contains tests for the custom methods added to the Newscatcher SDK client:
- get_all_articles
- get_all_headlines

These methods enhance the SDK by allowing retrieval of unlimited articles
through time-chunked requests.
"""

import sys
import os
import pytest
from unittest.mock import patch, MagicMock
import datetime
from typing import List, Dict, Any

# Add the src directory to the path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)

from newscatcher.client import NewscatcherApi, AsyncNewscatcherApi
from newscatcher.types.article_entity import ArticleEntity
from newscatcher.types.search_response_dto import SearchResponseDto


def create_mock_article(article_id: str, title: str) -> MagicMock:
    """Create a mock article with the given ID and title."""
    article = MagicMock(spec=ArticleEntity)
    article.id = article_id
    article.title = title
    article.score = 0.95
    return article


def create_mock_response(articles: List[MagicMock], total_pages: int = 1) -> MagicMock:
    """Create a mock search response with the given articles."""
    response = MagicMock(spec=SearchResponseDto)
    response.articles = articles
    response.total_pages = total_pages
    response.total_hits = len(articles)
    response.page = 1
    response.page_size = 10
    response.status = "ok"
    return response


class TestNewscatcherApiCustomMethods:
    """Tests for custom methods in NewscatcherApi."""

    def setup_method(self):
        """Set up test environment before each test."""
        self.client = NewscatcherApi(api_key="test_key")

    @patch("newscatcher.search.client.SearchClient.post")
    def test_get_all_articles_single_page(self, mock_post):
        """Test get_all_articles with a single page of results."""
        # Create mock articles
        mock_articles = [
            create_mock_article("1", "Article 1"),
            create_mock_article("2", "Article 2"),
        ]

        # Create mock response
        mock_response = create_mock_response(mock_articles)
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.get_all_articles(
            q="test", from_="1d", time_chunk_size="1d", max_articles=10
        )

        # Verify the results
        assert len(result) == 2
        assert result[0].id == "1"
        assert result[1].id == "2"
        assert mock_post.call_count == 1

    @patch("newscatcher.search.client.SearchClient.post")
    def test_get_all_articles_multiple_pages(self, mock_post):
        """Test get_all_articles with multiple pages of results."""
        # First page response
        first_page_articles = [
            create_mock_article("1", "Article 1"),
            create_mock_article("2", "Article 2"),
        ]
        first_page_response = create_mock_response(first_page_articles, total_pages=2)

        # Second page response
        second_page_articles = [
            create_mock_article("3", "Article 3"),
            create_mock_article("4", "Article 4"),
        ]
        second_page_response = create_mock_response(second_page_articles, total_pages=2)

        # Configure mock to return different responses
        mock_post.side_effect = [first_page_response, second_page_response]

        # Call the method
        result = self.client.get_all_articles(
            q="test", from_="1d", time_chunk_size="1d", max_articles=10
        )

        # Verify the results
        assert len(result) == 4
        assert [article.id for article in result] == ["1", "2", "3", "4"]
        assert mock_post.call_count == 2

    @patch("newscatcher.search.client.SearchClient.post")
    def test_get_all_articles_multiple_chunks(self, mock_post):
        """Test get_all_articles with multiple time chunks."""
        # Mock responses for the first chunk
        chunk1_page1 = create_mock_response(
            [create_mock_article("1", "Chunk 1, Article 1")]
        )

        # Mock responses for the second chunk
        chunk2_page1 = create_mock_response(
            [create_mock_article("2", "Chunk 2, Article 1")]
        )

        # Configure mock to return different responses for different chunks
        mock_post.side_effect = [chunk1_page1, chunk2_page1]

        # Set a small chunk size to force multiple chunks
        result = self.client.get_all_articles(
            q="test",
            from_="2d",  # 2 days ago
            to="1d",
            time_chunk_size="1d",  # 1-day chunks
            max_articles=10,
        )

        # Verify the results
        assert len(result) == 2
        assert result[0].id == "1"
        assert result[1].id == "2"
        assert mock_post.call_count == 2

    @patch("newscatcher.search.client.SearchClient.post")
    def test_get_all_articles_deduplication(self, mock_post):
        """Test get_all_articles deduplication functionality."""
        # Create duplicate articles across chunks
        chunk1_articles = [
            create_mock_article("1", "Article 1"),
            create_mock_article("2", "Article 2"),
        ]
        chunk1_response = create_mock_response(chunk1_articles)

        chunk2_articles = [
            create_mock_article("2", "Article 2"),
            create_mock_article("3", "Article 3"),
        ]
        chunk2_response = create_mock_response(chunk2_articles)

        # Configure mock
        mock_post.side_effect = [chunk1_response, chunk2_response]

        # Call with deduplication enabled
        result = self.client.get_all_articles(
            q="test", from_="2d", time_chunk_size="1d", deduplicate=True
        )

        # Verify duplicates were removed
        assert len(result) == 3
        assert [article.id for article in result] == ["1", "2", "3"]

        # Reset mock and call with deduplication disabled
        mock_post.reset_mock()
        mock_post.side_effect = [chunk1_response, chunk2_response]

        result_no_dedup = self.client.get_all_articles(
            q="test", from_="2d", time_chunk_size="1d", deduplicate=False
        )

        # Verify duplicates were kept
        assert len(result_no_dedup) == 4
        assert [article.id for article in result_no_dedup] == ["1", "2", "2", "3"]

    @patch("newscatcher.search.client.SearchClient.post")
    def test_get_all_articles_max_limit(self, mock_post):
        """Test get_all_articles respects max_articles limit."""
        # Create mock articles
        mock_articles1 = [
            create_mock_article(f"{i}", f"Article {i}") for i in range(1, 6)
        ]
        mock_articles2 = [
            create_mock_article(f"{i}", f"Article {i}") for i in range(6, 11)
        ]

        # Create mock responses
        mock_response1 = create_mock_response(mock_articles1, total_pages=2)
        mock_response2 = create_mock_response(mock_articles2, total_pages=2)

        # Configure mock
        mock_post.side_effect = [mock_response1, mock_response2]

        # Call with max_articles limit
        result = self.client.get_all_articles(
            q="test",
            from_="2d",
            time_chunk_size="1d",
            max_articles=7,  # Should stop after fetching 7 articles
        )

        # Verify limit was respected
        assert len(result) == 7
        assert [article.id for article in result] == ["1", "2", "3", "4", "5", "6", "7"]

    @patch("newscatcher.latestheadlines.client.LatestheadlinesClient.post")
    def test_get_all_headlines(self, mock_post):
        """Test get_all_headlines functionality."""
        # Create mock articles
        mock_articles = [
            create_mock_article("1", "Headline 1"),
            create_mock_article("2", "Headline 2"),
        ]

        # Create mock response
        mock_response = create_mock_response(mock_articles)
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.get_all_headlines(when="1d", time_chunk_size="1d")

        # Verify the results
        assert len(result) == 2
        assert result[0].id == "1"
        assert result[1].id == "2"
        assert mock_post.call_count == 1

        # Verify the when parameter was used
        args, kwargs = mock_post.call_args
        assert "when" in kwargs
        assert kwargs["when"] == "1d"


@pytest.mark.asyncio
class TestAsyncNewscatcherApiCustomMethods:
    """Tests for custom methods in AsyncNewscatcherApi."""

    def setup_method(self):
        """Set up test environment before each test."""
        self.client = AsyncNewscatcherApi(api_key="test_key")

    @patch("newscatcher.search.client.AsyncSearchClient.post")
    async def test_get_all_articles_async(self, mock_post):
        """Test async get_all_articles functionality."""
        # Create mock articles
        mock_articles = [
            create_mock_article("1", "Article 1"),
            create_mock_article("2", "Article 2"),
        ]

        # Create mock response
        mock_response = create_mock_response(mock_articles)
        mock_post.return_value = mock_response

        # Call the method
        result = await self.client.get_all_articles(
            q="test", from_="1d", time_chunk_size="1d"
        )

        # Verify the results
        assert len(result) == 2
        assert result[0].id == "1"
        assert result[1].id == "2"
        assert mock_post.call_count == 1

    @patch("newscatcher.search.client.AsyncSearchClient.post")
    async def test_get_all_articles_async_concurrency(self, mock_post):
        """Test async get_all_articles with concurrency for pagination."""
        # First page response
        first_page_articles = [create_mock_article("1", "Article 1")]
        first_page_response = create_mock_response(first_page_articles, total_pages=3)

        # Additional page responses
        page2_response = create_mock_response([create_mock_article("2", "Article 2")])
        page3_response = create_mock_response([create_mock_article("3", "Article 3")])

        # Configure mock
        mock_post.side_effect = [first_page_response, page2_response, page3_response]

        # Call the method with specified concurrency
        result = await self.client.get_all_articles(
            q="test", from_="1d", concurrency=2, time_chunk_size="1d"
        )

        # Verify the results
        assert len(result) == 3
        assert [article.id for article in result] == ["1", "2", "3"]
        assert mock_post.call_count == 3

    @patch("newscatcher.latestheadlines.client.AsyncLatestheadlinesClient.post")
    async def test_get_all_headlines_async(self, mock_post):
        """Test async get_all_headlines functionality."""
        # Create mock articles
        mock_articles = [
            create_mock_article("1", "Headline 1"),
            create_mock_article("2", "Headline 2"),
        ]

        # Create mock response
        mock_response = create_mock_response(mock_articles)
        mock_post.return_value = mock_response

        # Call the method
        result = await self.client.get_all_headlines(when="1d", time_chunk_size="1d")

        # Verify the results
        assert len(result) == 2
        assert result[0].id == "1"
        assert result[1].id == "2"
        assert mock_post.call_count == 1
