## [3.1.0] - 2026-09-30
### Added
- **`stream_reconnection_enabled`** and **`max_stream_reconnection_attempts`** — new optional constructor parameters on `BaseNewscatcherApi` and `AsyncBaseNewscatcherApi` (and matching fields on `RequestOptions`) to control automatic SSE stream reconnection with exponential backoff.
- **`get_keepalive_socket_options()`** — new helper that builds platform-appropriate TCP keepalive socket options to maintain long-lived connections through firewalls and NAT devices.
- **`RequestOptions.timeout`** — new `float` field as the preferred way to set per-request timeout in seconds; `timeout_in_seconds` is retained as a deprecated alias.
- **`BaseHttpResponse.response`** — new property exposing the underlying `httpx.Response` object for low-level response access.

### Changed
- **`EventSource`** — `iter_sse()` and `aiter_sse()` now automatically reconnect dropped SSE streams using the last event id, server-supplied `retry:` delay, and a configurable attempt budget; a 1 MiB per-line size guard prevents unbounded memory growth.
- **SSE parsing performance** — type-hint resolution, field-alias lookups, and `pydantic.TypeAdapter` construction are now cached per type, reducing overhead on high-throughput streaming paths; `parse_sse_obj` simplified to handle data-level discrimination only.
- **`Content-Type` header** — stripped from requests whose optional body resolves to empty, preventing spurious media-type headers on bodyless calls.
- **`aiohttp` / `httpx-aiohttp` dependencies** — minimum `aiohttp` raised to `>=3.14.1` and `httpx-aiohttp` widened to `^0.1.8`; both now require Python `>=3.10`.
- **NLP documentation links** — updated from "NLP features" to "NLP Enrichments" across `Theme`, `NotTheme`, `HasNlp`, `IncludeNlpData`, and sentiment type modules.

## 3.0.0 - 2026-05-19
### Breaking Changes
* **`NlpDataEntity.summary_translated`** — renamed to `translation_summary`; update all attribute access to use the new name (the JSON wire alias `summary_translated` is unchanged).
* **`AdditionalSourceInfo.nb_articles_for7d`** — renamed to `nb_articles_for_7_d`; update all attribute access to use the new name (the JSON wire alias `nb_articles_for_7d` is unchanged).
### Added
* **`max_retries`** — new optional constructor parameter on `BaseNewscatcherApi` and `AsyncBaseNewscatcherApi` to configure the default number of HTTP retries (defaults to 2); per-request `max_retries` in `RequestOptions` still takes precedence.
### Changed
* **`pydantic-core`** dependency upper bound widened from `<2.44.0` to `<3.0.0`, allowing use of newer pydantic-core releases.
* **`To` type alias** — union member order changed from `Union[dt.datetime, str]` to `Union[str, dt.datetime]`; no runtime impact for most callers.

## 2.1.1 - 2026-04-30
* fix: improve SSE line-ending normalization and incremental decoding
* Refactor the SSE event source to use Python's incremental codec decoder
* for correct multi-byte character handling across chunk boundaries, and
* add proper normalization of CR, LF, and CRLF line endings per the SSE
* specification. Also narrows the urllib3 dependency to >=2.6.3.
* Key changes:
* Add `_normalize_sse_line_endings()` to handle \r\n, bare \r, and \n uniformly
* Replace one-shot chunk decoding with `codecs.getincrementaldecoder` in both `iter_sse` and `aiter_sse`
* Flush incremental decoder at end of stream to avoid dropped trailing bytes
* Narrow urllib3 version constraint from `>=1.26.19,<2.0.0 || >=2.2.2,<3.0.0` to `>=2.6.3,<3.0.0`
* 🌿 Generated with Fern

