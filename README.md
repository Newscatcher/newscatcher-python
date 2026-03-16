# Newscatcher Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FNewscatcher%2Fnewscatcher-python)
[![pypi](https://img.shields.io/pypi/v/newscatcher-sdk)](https://pypi.python.org/pypi/newscatcher-sdk)

The Newscatcher Python library provides convenient access to the Newscatcher APIs from Python.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Retrieving More Articles](#retrieving-more-articles)
- [Query Validation](#query-validation)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Documentation

API reference documentation is available [here](https://www.newscatcherapi.com/docs/news-api/api-reference/overview).

## Installation

```sh
pip install newscatcher-sdk
```

## Reference

A full reference for this library is available [here](https://github.com/Newscatcher/newscatcher-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    api_key="<value>",
)

client.search.post(
    q="\"supply chain\" AND Amazon NOT China",
    page_size=1,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from newscatcher import AsyncNewscatcherApi

client = AsyncNewscatcherApi(
    api_key="<value>",
)


async def main() -> None:
    await client.search.post(
        q="\"supply chain\" AND Amazon NOT China",
        page_size=1,
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

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

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(...)
response = client.search.with_raw_response.post(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.search.post(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from newscatcher import NewscatcherApi

client = NewscatcherApi(..., timeout=20.0)

# Override timeout for a specific method
client.search.post(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from newscatcher import NewscatcherApi

client = NewscatcherApi(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
