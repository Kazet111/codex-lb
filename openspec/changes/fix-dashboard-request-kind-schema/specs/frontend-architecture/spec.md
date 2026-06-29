## ADDED Requirements

### Requirement: Dashboard request logs accept backend request kinds

The dashboard request-log client schema MUST accept any non-empty `requestKind` string returned by `GET /api/request-logs`. The dashboard MUST continue to default omitted legacy `requestKind` fields to `normal`. Known request-kind values MAY receive custom labels, and unknown request-kind values MUST NOT cause the dashboard response schema validation to fail.

#### Scenario: Non-enumerated request kind does not block dashboard

- **WHEN** `GET /api/request-logs` returns a request row with `requestKind: "prewarm"`
- **THEN** the dashboard request-log schema accepts the response
- **AND** the parsed row preserves `requestKind: "prewarm"`

#### Scenario: Legacy omitted request kind still defaults

- **WHEN** `GET /api/request-logs` returns a request row without `requestKind`
- **THEN** the dashboard request-log schema accepts the response
- **AND** the parsed row uses `requestKind: "normal"`
