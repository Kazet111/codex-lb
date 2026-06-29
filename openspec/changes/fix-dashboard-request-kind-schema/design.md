## Context

The backend stores request-kind metadata as an open string because internal proxy workflows can introduce values beyond the original three dashboard labels. The frontend independently narrowed the field to a closed enum, causing the entire request-log response to fail validation when any row used a newer kind.

## Goals / Non-Goals

**Goals:**

- Keep response validation strict about the field being a non-empty string.
- Accept backend-defined request kinds without requiring synchronized frontend releases.
- Preserve the legacy omitted-field default.

**Non-Goals:**

- Enumerate every internal request kind in the frontend.
- Change backend persistence or response contracts.
- Add custom labels for every internal kind.

## Decisions

- Replace the closed Zod enum with `z.string().min(1)` because the backend contract is intentionally extensible.
- Keep `.optional().default("normal")` so older responses retain their existing behavior.
- Preserve presentation fallback behavior: known kinds use labels and unknown kinds render their raw value.

Expanding the enum with `prewarm` alone was rejected because the next internal request kind would recreate the same failure.

## Risks / Trade-offs

- [Risk] Misspelled backend request kinds render as raw text. -> The backend remains the contract owner, and non-empty validation still rejects structurally invalid values.
- [Risk] A future display path assumes only known kinds. -> Regression coverage preserves a non-enumerated value through parsing.

## Migration Plan

Rebuild the frontend bundle and deploy it with the existing backend. No database or API migration is required. Rollback restores the prior frontend bundle but also restores the response-rejection bug.

## Open Questions

None.
