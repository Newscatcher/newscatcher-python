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

