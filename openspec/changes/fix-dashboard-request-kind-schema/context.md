# Dashboard Request-Kind Compatibility

## Purpose and Scope

This change keeps the dashboard compatible with request-kind metadata owned by the backend. It affects only client-side parsing of request-log responses and does not widen unrelated fields.

## Decision and Constraints

The backend field is an extensible, non-empty string. The frontend therefore validates its structure rather than duplicating a closed list. Omitted legacy values still default to `normal`, and existing known-value labels remain unchanged.

## Failure Mode

Before this change, one row with a newer kind caused Zod to reject the entire response. The API still returned HTTP 200, while the dashboard showed `Response schema mismatch` and lost the recent-requests view.

## Example

`requestKind: "prewarm"` is accepted and preserved. The table can render the raw value when no friendly label exists.

## Operational Note

This fix requires a rebuilt frontend bundle. No database migration, data rewrite, or backend rollout is needed.
