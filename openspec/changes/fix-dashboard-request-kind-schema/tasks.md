## 1. Spec

- [x] 1.1 Document that dashboard request-log parsing accepts backend request-kind strings beyond the historical warmup values.

## 2. Implementation

- [x] 2.1 Update the frontend request-log schema to accept any non-empty request-kind string.
- [x] 2.2 Preserve the omitted-field default for legacy responses.

## 3. Verification

- [x] 3.1 Add schema coverage for a non-enumerated request kind.
- [x] 3.2 Run targeted frontend schema tests.
- [x] 3.3 Run strict OpenSpec validation.
- [x] 3.4 Build the combined Docker image and verify the dashboard response against the existing data volume.
