# Architecture

```mermaid
flowchart LR
  Reviewer --> UI[React evidence workspace]
  UI --> API[FastAPI + Pydantic]
  API --> Claims[(SQLite claim records)]
  API --> Evidence[(Source metadata and passages)]
  Claims --> Reports[Verdict counts and source coverage]
```

The reviewer controls claim boundaries and verdicts. The API validates claim and source fields, stores evidence notes and labels, and derives simple coverage summaries. It does not fetch source pages, infer verdicts, or mark an unsupported claim false. Source quality dimensions are human-entered metadata.

SQLite and the local sample corpus make this a review-workflow prototype. Authentication, source snapshotting, automated claim extraction, and durable cloud persistence are not implemented.
