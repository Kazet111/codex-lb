## Why

The dashboard recent request-log query can return request rows whose `requestKind` is internal proxy metadata such as `prewarm`, `compaction`, `thread_goal_*`, or `codex_control_*`. The frontend request-log schema only accepts `normal`, `warmup`, and `limit_warmup`, so a valid `GET /api/request-logs` response can be rejected as `Response schema mismatch` and leave the dashboard without its primary view.

## What Changes

- Allow the dashboard request-log client schema to accept any non-empty `requestKind` string returned by the backend.
- Preserve the existing default of `normal` when older responses omit the field.
- Keep known request-kind labels, while letting unknown kinds render through the existing formatted fallback.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `frontend-architecture`: Accept backend-defined request-kind metadata without rejecting the dashboard response.

## Impact

- Frontend: dashboard request-log response parsing.
- Tests: request-log schema coverage for non-enumerated request kinds.
- APIs and dependencies: no changes.
