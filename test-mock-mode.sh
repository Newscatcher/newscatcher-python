#!/bin/bash
# Run tests in mock mode

# Generate mock data
echo "Generating mock data..."
python -c "$(cat << 'EOF'
import os
import json
from pathlib import Path
import datetime

# Ensure the mocks directory exists
mock_dir = Path("tests/mocks")
os.makedirs(mock_dir, exist_ok=True)

# Generate mock search response
search_mock = {
    "status": "ok",
    "total_hits": 12000,  # Above API limit to test the limit bypass
    "total_pages": 120,
    "page": 1,
    "page_size": 100,
    "articles": []
}

# Generate mock article data for different dates
# Create dates across a 90-day period
current_date = datetime.datetime.now()
for i in range(100):
    # Create articles with different dates
    days_ago = i % 90  # Spread across 90 days
    article_date = (current_date - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    article = {
        "id": f"mock_search_{i}",
        "title": f"Mock Search Article {i}",
        "summary": f"This is a mock summary for search article {i}",
        "published_date": article_date,
        "link": f"https://example.com/search/{i}",
        "language": "en" if i % 3 == 0 else ("es" if i % 3 == 1 else "fr"),  # Mix of languages
        "author": f"Mock Author {i % 10}",
        "authors": [f"Mock Author {i % 10}"],
        "name_source": f"Mock Source {i % 5}",
        "score": round(0.99 - (i * 0.005), 2),
    }
    search_mock["articles"].append(article)

# Save search mock
with open(mock_dir / "search.json", "w") as f:
    json.dump(search_mock, f, indent=2)

# Generate mock latestheadlines response
headlines_mock = {
    "status": "ok",
    "total_hits": 8000,
    "total_pages": 80,
    "page": 1,
    "page_size": 100,
    "articles": []
}

# Generate mock headline data
for i in range(100):
    # Create articles with different dates
    days_ago = i % 30  # Headlines are more recent, only 30 days
    article_date = (current_date - datetime.timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    article = {
        "id": f"mock_headline_{i}",
        "title": f"Mock Headline Article {i}",
        "summary": f"This is a mock summary for headline {i}",
        "published_date": article_date,
        "link": f"https://example.com/headline/{i}",
        "language": "en" if i % 4 == 0 else ("es" if i % 4 == 1 else ("fr" if i % 4 == 2 else "de")),  # Mix of languages
        "author": f"Headline Author {i % 8}",
        "authors": [f"Headline Author {i % 8}"],
        "name_source": f"Headline Source {i % 7}",
        "score": round(0.99 - (i * 0.003), 2),
    }
    headlines_mock["articles"].append(article)

# Save headlines mock
with open(mock_dir / "latestheadlines.json", "w") as f:
    json.dump(headlines_mock, f, indent=2)

print(f"Created mock data files in {mock_dir}:")
print(f"- search.json: {len(search_mock['articles'])} articles")
print(f"- latestheadlines.json: {len(headlines_mock['articles'])} articles")
EOF
)"

# Run tests in mock mode
echo "Running tests in mock mode..."
TEST_MODE=mock python -m pytest tests/custom tests/integration -v

# Check results
if [ $? -eq 0 ]; then
    echo "✅ Tests passed in mock mode!"
else
    echo "❌ Tests failed in mock mode."
fi