# Product requirements and acceptance criteria

## Problem and users

Reviewers need to decompose an answer into claims, record evidence and scope, and distinguish contradiction from uncertainty. Users are fact-checkers, research reviewers, and annotation teams.

## MVP behavior

1. Store editable claim-level records linked to an answer.
2. Record source title, URL, access date, passage, scope, and reviewer-entered authority/directness/freshness/relevance.
3. Support supported, contradicted, unresolved, and not-checkable outcomes.
4. Search/filter claims and summarize verdict counts and source coverage.
5. Seed examples that exercise stable facts, time-sensitive claims, fabricated figures, unsupported causality, and opinions.

## Acceptance checks

- Claims without evidence can remain unresolved; absence of a citation alone never triggers a false label.
- Contradicted judgments retain a passage that directly conflicts with the claim.
- Source scope and access date are visible in stored records and exports.
- Tests cover all verdicts and validation; the frontend build passes.

## Risks and limits

The app does not fetch or archive sources, split claims automatically, or verify reviewer-entered source quality. It has no authentication. Time-sensitive claims require fresh external research at review time. Example source notes are illustrative evidence, not a general automated fact-checking result.
