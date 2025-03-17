#!/bin/bash
# Run tests in mock mode

# Generate mock data
echo "Generating mock data..."
python -c "$(cat << 'EOF'
"""
Script to generate mock data files for testing.

This script creates mock response files that match the actual Newscatcher API
response structure to ensure tests have realistic data.
"""

import os
import json
from pathlib import Path
import datetime
import random

# Ensure the mocks directory exists
mock_dir = Path("tests/mocks")
os.makedirs(mock_dir, exist_ok=True)

# Generate mock search response
search_mock = {
    "status": "ok",
    "total_hits": 10000,  # Using the API limit value
    "page": 1,
    "total_pages": 10000,
    "page_size": 100,
    "articles": []
}

# Sample domains and sources
domains = ["usatoday.com", "bbc.co.uk", "nytimes.com", "reuters.com", "theguardian.com", "cnn.com"]
sources = ["USA TODAY", "BBC News", "The New York Times", "Reuters", "The Guardian", "CNN"]
countries = ["US", "GB", "US", "GB", "GB", "US"]
ranks = [155, 80, 125, 95, 110, 120]

# Generate mock article data
current_date = datetime.datetime.now()
for i in range(100):
    # Create articles with different dates
    days_ago = i % 90  # Spread across 90 days
    article_date = (current_date - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M:%S")
    
    # Pick a random source
    idx = i % len(domains)
    
    article = {
        "title": f"Mock Search Article {i}: Tech news for today",
        "author": f"Mock Author {i % 10}" if i % 3 != 0 else "",
        "authors": [f"Mock Author {i % 10}"] if i % 3 != 0 else [],
        "journalists": [],
        "published_date": article_date,
        "published_date_precision": "full" if i % 2 == 0 else "timezone unknown",
        "updated_date": article_date if i % 4 == 0 else None,
        "updated_date_precision": "full" if i % 4 == 0 else None,
        "link": f"https://www.{domains[idx]}/story/{i}",
        "domain_url": domains[idx],
        "full_domain_url": f"www.{domains[idx]}",
        "name_source": sources[idx],
        "is_headline": i % 10 == 0,
        "paid_content": i % 20 == 0,
        "parent_url": f"https://www.{domains[idx]}/story",
        "country": countries[idx],
        "rights": domains[idx],
        "rank": ranks[idx],
        "media": f"https://www.{domains[idx]}/images/image{i}.jpg" if i % 3 == 0 else None,
        "language": "en" if i % 5 != 1 else ("es" if i % 5 == 1 else "fr"),
        "description": f"This is a mock description for article {i}. It contains tech-related content.",
        "content": f"This is mock content for article {i}. It is designed to simulate a real article from the Newscatcher API. This content would normally be much longer and contain detailed information about a news story.",
        "word_count": random.randint(100, 1000),
        "is_opinion": i % 10 == 5,
        "twitter_account": f"@{domains[idx].split('.')[0]}" if i % 3 == 0 else None,
        "all_links": [
            f"https://www.facebook.com/{domains[idx].split('.')[0]}",
            f"https://www.twitter.com/{domains[idx].split('.')[0]}"
        ] if i % 2 == 0 else [],
        "all_domain_links": [
            "facebook.com",
            "twitter.com"
        ] if i % 2 == 0 else [],
        "id": f"mock_search_{i}_" + "".join(random.choice("abcdef0123456789") for _ in range(24)),
        "score": round(10.0 - (i * 0.1), 2) if i < 100 else 0.0
    }
    search_mock["articles"].append(article)

# Include user_input field in the search response as seen in the example
search_mock["user_input"] = {
    "q": "tech",
    "search_in": ["title_content"],
    "predefined_sources": None,
    "sources": None,
    "not_sources": None,
    "lang": None,
    "not_lang": None,
    "countries": None,
    "not_countries": None,
    "not_author_name": None,
    "from_": (current_date - datetime.timedelta(days=1)).isoformat(),
    "to_": current_date.isoformat(),
    "published_date_precision": None,
    "by_parse_date": False,
    "sort_by": "relevancy",
    "ranked_only": None,
    "from_rank": None,
    "to_rank": None,
    "is_headline": None,
    "is_opinion": None,
    "is_paid_content": False,
    "parent_url": None,
    "all_links": None,
    "all_domain_links": None,
    "word_count_min": None,
    "word_count_max": None,
    "page": 1,
    "page_size": "100",
    "clustering_variable": None,
    "clustering_enabled": None,
    "clustering_threshold": None,
    "include_nlp_data": None,
    "has_nlp": None,
    "theme": None,
    "not_theme": None,
    "ORG_entity_name": None,
    "PER_entity_name": None,
    "LOC_entity_name": None,
    "MISC_entity_name": None,
    "title_sentiment_min": None,
    "title_sentiment_max": None,
    "content_sentiment_min": None,
    "content_sentiment_max": None,
    "iptc_tags": None,
    "not_iptc_tags": None,
    "source_name": None,
    "iab_tags": None,
    "not_iab_tags": None,
    "exclude_duplicates": None,
    "additional_domain_info": None,
    "is_news_domain": None,
    "news_domain_type": None,
    "news_type": None
}

# Save search mock
with open(mock_dir / "search.json", "w") as f:
    json.dump(search_mock, f, indent=2)

# Generate mock latestheadlines response
headlines_mock = {
    "status": "ok",
    "total_hits": 10000,
    "page": 1,
    "total_pages": 10000,
    "page_size": 100,
    "articles": []
}

# Generate mock headline data
for i in range(100):
    # Create articles with different dates
    days_ago = i % 30  # Headlines are more recent, only 30 days
    article_date = (current_date - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M:%S")
    
    # Pick a random source
    idx = i % len(domains)
    
    article = {
        "title": f"Mock Headline {i}: Breaking news today",
        "author": f"Headline Author {i % 8}" if i % 4 != 0 else "News Agency",
        "authors": [f"Headline Author {i % 8}"] if i % 4 != 0 else ["News Agency"],
        "journalists": [],
        "published_date": article_date,
        "published_date_precision": "timezone unknown" if i % 2 == 0 else "full",
        "updated_date": None,
        "updated_date_precision": None,
        "link": f"https://www.{domains[idx]}/{i}",
        "domain_url": domains[idx],
        "full_domain_url": f"www.{domains[idx]}",
        "name_source": sources[idx],
        "is_headline": True,
        "paid_content": False,
        "parent_url": f"https://www.{domains[idx]}/headlines",
        "country": countries[idx],
        "rights": domains[idx],
        "rank": ranks[idx],
        "media": None,
        "language": "en" if i % 5 != 2 else ("fr" if i % 5 == 2 else "es"),
        "description": f"Mock headline {i} description. Breaking news coverage.",
        "content": f"Content for headline {i}. This simulates the content of a breaking news story from the Newscatcher API.",
        "word_count": random.randint(50, 500),
        "is_opinion": False,
        "twitter_account": None,
        "all_links": [],
        "all_domain_links": [],
        "id": f"mock_headline_{i}_" + "".join(random.choice("abcdef0123456789") for _ in range(24)),
        "score": 0.0
    }
    headlines_mock["articles"].append(article)

# Include user_input field in the headlines response as seen in the example
headlines_mock["user_input"] = {
    "when": current_date.isoformat(),
    "by_parse_date": False,
    "sort_by": "relevancy",
    "lang": ["en"],
    "not_lang": None,
    "countries": None,
    "not_countries": None,
    "sources": None,
    "predefined_sources": None,
    "not_sources": None,
    "not_author_name": None,
    "ranked_only": None,
    "is_headline": None,
    "is_opinion": None,
    "is_paid_content": None,
    "parent_url": None,
    "all_links": None,
    "all_domain_links": None,
    "word_count_min": None,
    "word_count_max": None,
    "page": 1,
    "page_size": "100",
    "clustering_variable": None,
    "clustering_enabled": None,
    "clustering_threshold": None,
    "include_nlp_data": None,
    "has_nlp": None,
    "embeddings_output": None,
    "theme": None,
    "not_theme": None,
    "ORG_entity_name": None,
    "PER_entity_name": None,
    "LOC_entity_name": None,
    "MISC_entity_name": None,
    "title_sentiment_min": None,
    "title_sentiment_max": None,
    "content_sentiment_min": None,
    "content_sentiment_max": None,
    "iptc_tags": None,
    "not_iptc_tags": None,
    "iab_tags": None,
    "not_iab_tags": None
}

# Save headlines mock
with open(mock_dir / "latestheadlines.json", "w") as f:
    json.dump(headlines_mock, f, indent=2)

print(f"Created mock data files in {mock_dir}:")
print(f"- search.json: {len(search_mock['articles'])} articles")
print(f"- latestheadlines.json: {len(headlines_mock['articles'])} articles")
EOF
)"

# Add tests/mocks to .gitignore if not already there
if ! grep -q "tests/mocks" .gitignore; then
    echo -e "\n# Mock test data\ntests/mocks/" >> .gitignore
    echo "Added tests/mocks/ to .gitignore"
fi

# Add tests/data to .gitignore if not already there
if ! grep -q "tests/data" .gitignore; then
    echo -e "\n# Test data cache\ntests/data/" >> .gitignore
    echo "Added tests/data/ to .gitignore"
fi

# Run tests in mock mode
echo "Running tests in mock mode..."
TEST_MODE=mock python -m pytest tests/custom tests/integration -v

# Check results
if [ $? -eq 0 ]; then
    echo "✅ Tests passed in mock mode!"
else
    echo "❌ Tests failed in mock mode."
fi