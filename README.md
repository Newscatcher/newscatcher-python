# Newscatcher Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FNewscatcher%2Fnewscatcher-python)
[![pypi](https://img.shields.io/pypi/v/newscatcher-sdk)](https://pypi.python.org/pypi/newscatcher-sdk)

The Newscatcher Python library provides convenient access to the Newscatcher API from Python.

## Documentation

API reference documentation is available [here](https://www.newscatcherapi.com/docs/v3/api-reference).

## Installation

```sh
pip install newscatcher-sdk
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

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

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

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

## Retrieving More Articles

The standard News API endpoints have a limit of 10,000 articles per query. To help retrieve more articles when needed, this SDK provides methods that automatically break down your request into smaller time chunks:

### Get All Articles

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

### Get All Latest Headlines

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

These methods handle pagination and deduplication automatically, providing a seamless experience for retrieving large datasets.

The async versions of these methods are also available with the `AsyncNewscatcherApi` client.

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

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

client = NewscatcherApi(
    ...,
    timeout=20.0,
)


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
        proxies="http://my.test.proxy.example.com",
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
