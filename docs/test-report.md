# Test report — 2026-10-28

Environment: Windows host, bundled Python 3.12.14, pytest 8.3.5, Node.js 22, npm 10.9.x, Vite 6.4.5.

| Check | Result | Evidence |
|---|---|---|
| Backend unit and data validation tests | **6 passed, 0 failed, 0 skipped** | `python -m pytest -q` |
| Synthetic dataset validation | **Passed** | All 7 examples validate and cover all 4 verdict labels |
| Frontend production build | **Passed** | `npm run build`; TypeScript and Vite succeeded |
| Lint / type check | **No separate lint configured; TypeScript type check passed** | `tsc -b` runs as part of the production build; no Python static type checker is configured |
| API live smoke check | **Passed** | Seeded 7 example claims; source coverage 0.714; created a supported claim and retrieved its source evidence |
| Manual browser workflow | **Passed at the current browser viewport** | Displayed 7 seeded claims and saved a source-free claim as unresolved with a rationale |
| Deployment | **Not deployed** | No remote host configured |
| GitHub publication | **Published** | Public GitHub snapshot on `main`; source files verified |

The examples demonstrate supported, contradicted, unresolved, and not-checkable judgments using synthetic claim records and actual official-source evidence passages. The unresolved status is preserved for unsupported or time-sensitive claims; no automated false verdict is produced.

Known gaps: no external source fetching, archived snapshots, systematic desktop/mobile breakpoint matrix, authentication, or deployed smoke test. Source assessment fields are manually entered and are not independently verified by the application.

