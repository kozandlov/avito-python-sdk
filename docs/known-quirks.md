# Known OpenAPI Quirks

## 1) auth `/token` duplicated with hidden unicode

Some `auth` specs expose path keys that visually match `/token` but differ by hidden unicode marks.

Normalization rule:
- Strip invisible unicode chars from path keys.
- Collapse all token-like paths to exact `/token`.

## 2) messenger `sendMessageRequestBody.required`

In some snapshots, `sendMessageRequestBody.required` includes `url`, while schema properties do not contain `url`.

Normalization rule:
- For `sendMessageRequestBody`, set `required = ["type", "message"]` when schema contains these properties.

## 3) Missing operationId / collisions

Some operations may have missing or duplicate operationId across API groups.

Normalization rule:
- Generate deterministic operationId as `{method}_{normalized_path}` if missing.
- If duplicated, suffix with `_2`, `_3`, ... preserving deterministic order.
