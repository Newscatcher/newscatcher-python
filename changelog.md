## [3.1.0] - 2026-10-22
### Added
- **`get_keepalive_socket_options()`** — new helper that builds cross-platform TCP keepalive socket options for use with `httpx.HTTPTransport` to keep idle connections alive through firewalls and NAT.
- **`quote_path_param()`** — new URL-encoding helper that percent-encodes path parameters and rejects dot-segments to prevent path-traversal issues.
- **SSE auto-reconnect** — `EventSource` now supports automatic stream reconnection with configurable max attempts, exponential backoff, and `Last-Event-ID` resumption for both sync and async consumers.
- **`stream_reconnection_enabled`**, **`max_stream_reconnection_attempts`**, **`retry_remote_protocol_errors`**, and **`timeout`** — new per-request fields on `RequestOptions` and optional constructor parameters on `BaseNewscatcherApi` / `AsyncBaseNewscatcherApi` for fine-grained retry and reconnection control.
- **`NewsDomainTypeOneItem`** and **`BaseHttpResponse.response`** — new exported type for `news_domain_type` literals and new property exposing the underlying `httpx.Response` object directly.

### Changed
- **`RemoteProtocolError` retry behavior** — `RemoteProtocolError` is no longer retried automatically; opt in by setting `retry_remote_protocol_errors: True` in `RequestOptions`.
- **Header merging** — `additional_headers` in `RequestOptions` now uses case-insensitive merging, preventing duplicate headers when keys differ only by case.
- **`x-api-token` redaction** — the `x-api-token` header is now redacted in debug logs alongside other sensitive headers.
- **SSE line size limit** — SSE streams now raise `SSEError` when a single line exceeds 1 MiB, preventing unbounded memory growth on malformed streams.

### Fixed
- **`news_domain_type` serialization** — the `news_domain_type` parameter in search and sources endpoints now correctly serializes enum values via `convert_and_respect_annotation_metadata`, matching the behavior of `news_type`.

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

