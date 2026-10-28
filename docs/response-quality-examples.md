# Response-quality examples

These examples show how response-quality concerns become claim-level review decisions. The evidence desk stores reviewer judgments; it does not automatically fact-check prose.

| Category | Sample answer/claim | Evidence treatment |
|---|---|---|
| Correct | “Earth takes about 365.25 days to orbit the Sun.” | **Supported** by NASA's [Earth facts page](https://science.nasa.gov/earth/facts/), which states the orbital trip takes 365.25 days. |
| Incorrect | “Earth takes 365.25 days to rotate once on its axis.” | **Contradicted** by the same NASA page, which distinguishes a 23.9-hour rotation from the 365.25-day orbit. |
| Incomplete | “Earth has seasons.” in response to “What causes the yearly seasons?” | The statement is true but does not answer the causal question; annotate the missing explanation separately from factuality. |
| Misleading | “Earth's 365.25-day orbit causes the seasons.” | Keep **unresolved/unsupported** unless direct evidence settles it; NASA attributes the yearly cycle to axial tilt. Avoid turning insufficient evidence into a false verdict. |
| Ambiguous | “It is summer when Earth is closest to the Sun.” | Ask which hemisphere and what “summer” means; without scope, preserve ambiguity instead of asserting a universal claim. |
| Poorly formatted | Requested JSON `{"claim":"...","source":...}`; response: `{"claim":"Earth orbits the Sun", "source":}` | Mark the output-format defect separately; do not treat malformed syntax as evidence that the underlying claim is false. |

The examples use real source titles and quoted passages in the sample corpus. Access date and passage scope must remain attached to each verdict. A source's reputation alone is not direct support.
