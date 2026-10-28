# Claim review methodology

## Workflow

1. Split a generated answer into atomic, independently checkable claims. Keep qualifiers and scope in the claim text.
2. Identify the evidence needed to verify each claim. Prefer primary sources (official documentation, original data, or the responsible institution).
3. Record the exact passage, source scope, URL, and access date. Score authority, directness, freshness, and relevance from 1–5.
4. Choose a verdict: **supported** (direct evidence supports the claim), **contradicted** (direct evidence conflicts), **unresolved** (evidence is missing, conflicting, stale, or insufficient), or **not checkable** (subjective or too vague to operationalize).
5. Explain how the passage supports the verdict and state any remaining uncertainty.

Missing evidence does not mean false. The app enforces that supported and contradicted labels include at least one source record; it does not decide whether the source truly supports the claim.

## Source-quality dimensions

- Authority: is this source accountable and competent for the claim?
- Directness: does the passage address this exact claim?
- Freshness: is it timely enough for the claim?
- Relevance: does it cover the same population, period, and scope?

Ratings are reviewer judgments, not a proof score. A high source-quality total cannot replace a claim-specific passage.

## Metrics

Source coverage is `(claims with one or more source records) / (all claims)` and is undefined for an empty dataset. Verdict counts and missing-source counts describe only the current local dataset. They do not measure model quality or error prevalence.

## Examples and evidence provenance

The synthetic fixtures cite NASA's [Facts About Earth](https://science.nasa.gov/earth/facts/) for orbital period and rotation, and the Python documentation's [Data Structures tutorial](https://docs.python.org/3/tutorial/datastructures.html) for list mutability. Passages and scopes are included in `data/examples.json` and were checked on 2026-10-28. Time-sensitive and subjective examples are intentionally unresolved or not-checkable.
