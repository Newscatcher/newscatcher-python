## [3.1.0] - 2026-08-04
### Added
- **`stream_reconnection_enabled`** and **`max_stream_reconnection_attempts`** — new optional constructor parameters on `BaseNewscatcherApi` and `AsyncBaseNewscatcherApi` (and per-request fields in `RequestOptions`) to configure automatic SSE stream reconnection with exponential backoff.
- **`RequestOptions.timeout`** — new `float` field for per-request timeouts in seconds; supersedes the now-deprecated `timeout_in_seconds` alias when both are provided.
- **`get_keepalive_socket_options()`** — new helper that builds cross-platform TCP keepalive socket options for use with httpx transports to keep long-lived connections alive through firewalls and NAT.
- **`quote_path_param()`** — new utility in `jsonable_encoder` that percent-encodes path segment values to prevent path-traversal issues.

### Changed
- **`EventSource`** — `iter_sse` and `aiter_sse` now automatically reconnect resumable streams on transport errors, tracking the last dispatched event id and resetting the attempt counter on each successfully dispatched event.
- **`parse_sse_obj`** — simplified to data-level discrimination only; protocol-level SSE `event:` field discrimination is now handled at code-generation time, removing internal `_get_discriminator_and_variants` helpers.
- **Serialization performance** — `convert_and_respect_annotation_metadata` now caches resolved type hints and short-circuits recursive walks when no `FieldMetadata` aliases are present, reducing overhead on SSE streaming hot paths.
- **`aiohttp` / `httpx-aiohttp` dependencies** — minimum `aiohttp` raised to `>=3.14.1`, `httpx-aiohttp` widened to `^0.1.8`, both now requiring Python `>=3.10`.

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

