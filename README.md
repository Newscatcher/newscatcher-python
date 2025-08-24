# Newscatcher Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FNewscatcher%2Fnewscatcher-python)
[![pypi](https://img.shields.io/pypi/v/newscatcher-sdk)](https://pypi.python.org/pypi/newscatcher-sdk)

The Newscatcher Python library gives you convenient access to the Newscatcher API from Python.

## Documentation

View API reference documentation at [newscatcherapi.com/docs](https://www.newscatcherapi.com/docs/v3/api-reference).

## Installation

```sh
pip install newscatcher-sdk
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Create and use the client:

```python
import datetime

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="YOUR_API_KEY",
)
client.search.post(
    q="renewable energy",
    predefined_sources=["top 50 US"],
    lang=["en"],
    from_=datetime.datetime.fromisoformat(
        "2024-01-01 00:00:00+00:00",
    ),
    to=datetime.datetime.fromisoformat(
        "2024-06-30 00:00:00+00:00",
    ),
    additional_domain_info=True,
    is_news_domain=True,
)
```

## Async client

Use the `AsyncNewscatcherApi` client to make non-blocking calls to the API:

```python
import asyncio
import datetime

from newscatcher import AsyncNewscatcherApi

client = AsyncNewscatcherApi(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.search.post(
        q="renewable energy",
        predefined_sources=["top 50 US"],
        lang=["en"],
        from_=datetime.datetime.fromisoformat(
            "2024-01-01 00:00:00+00:00",
        ),
        to=datetime.datetime.fromisoformat(
            "2024-06-30 00:00:00+00:00",
        ),
        additional_domain_info=True,
        is_news_domain=True,
    )


asyncio.run(main())
```

## Exception handling

The SDK raises an `ApiError` when the API returns a non-success status code (4xx or 5xx response):

```python
from newscatcher.core.api_error import ApiError

try:
    client.search.post(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Retrieving more articles

The standard News API endpoints have a limit of 10,000 articles per query. To retrieve more articles when needed, use these methods that automatically break down your request into smaller time chunks:

### Get all articles

```python
import datetime
from newscatcher import NewscatcherApi

client = NewscatcherApi(api_key="YOUR_API_KEY")

# Get articles about renewable energy from the past 10 days
articles = client.get_all_articles(
    q="renewable energy",
    from_="10d",  # Last 10 days
    time_chunk_size="1d",  # Split into 1-day chunks
    max_articles=50000,    # Limit to 50,000 articles
    show_progress=True     # Show progress indicator
)

print(f"Retrieved {len(articles)} articles")
```

### Get all latest headlines

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(api_key="YOUR_API_KEY")

# Get all technology headlines from the past week
articles = client.get_all_headlines(
    when="7d",
    time_chunk_size="1h",  # Split into 1-hour chunks
    show_progress=True
)

print(f"Retrieved {len(articles)} articles")
```

These methods handle pagination and deduplication automatically, giving you a seamless experience for retrieving large datasets.

You can also use async versions of these methods with the `AsyncNewscatcherApi` client.

## Query validation

The SDK includes client-side query validation to help you catch syntax errors before making API calls:

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(api_key="YOUR_API_KEY")

# Validate query syntax
is_valid, error_message = client.validate_query("machine learning")
if is_valid:
    print("Query is valid!")
else:
    print(f"Invalid query: {error_message}")
```

### Automatic validation

Query validation is enabled by default in methods like `get_all_articles()` and will raise a `ValueError` for invalid queries. You can disable validation by setting `validate_query=False`:

```python
# Enable validation (default)
articles = client.get_all_articles(
    q="AI OR \"artificial intelligence\"",  # Valid query
    validate_query=True,  # Optional, True by default
    from_="7d"
)

# Disable validation (not recommended)
articles = client.get_all_articles(
    q="some query",
    validate_query=False,  # Skip client-side validation
    from_="7d"
)
```

For complete validation rules, bulk validation techniques, and troubleshooting, see [Validate queries with Python SDK](https://www.newscatcherapi.com/docs/v3/documentation/how-to/validate-queries-python-sdk).

## Advanced

### Retries

The SDK includes automatic retries with exponential backoff. The SDK retries a request when the request is retriable and the number of retry attempts is less than the configured retry limit (default: 2).

The SDK retries requests when the API returns these HTTP status codes:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior:

```python
client.search.post(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK uses a 60-second timeout by default. Configure timeouts at the client or request level:

```python

from newscatcher import NewscatcherApi

client = NewscatcherApi(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.search.post(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom client

Override the `httpx` client to customize it for your use case. Common use cases include proxies and transports:

```python
import httpx
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

We value open-source contributions to this SDK. This library is generated programmatically, but we can implement custom methods and use `.fernignore` to preserve certain files. However, implementing custom solutions in the SDK involves a complex process. Please open an issue first to discuss your ideas before submitting a PR.

On the other hand, contributions to the README are always very welcome!
