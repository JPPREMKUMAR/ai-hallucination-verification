import pytest
import json
from pathlib import Path
from pydantic import ValidationError
from app import storage
from app.models import ClaimInput

def valid_claim(**changes):
    record={"id":"x","text":"A factual claim for review.","category":"test","verdict":"unresolved","rationale":"The evidence is not sufficient to decide this claim.","sources":[]}
    record.update(changes);return ClaimInput.model_validate(record)

def test_unresolved_without_source_is_valid_and_not_false():
    storage.save_claim(valid_claim())
    assert storage.report()["verdict_counts"]=={"unresolved":1}

def test_supported_requires_evidence():
    with pytest.raises(ValidationError,match="require evidence"):
        valid_claim(verdict="supported")

def test_source_quality_fields_are_bounded():
    with pytest.raises(ValidationError):
        valid_claim(verdict="supported",sources=[{"title":"Source","url":"https://example.org","accessed_at":"2026-10-28","evidence_passage":"A passage.","scope":"Scope.","authority":6,"directness":4,"freshness":4,"relevance":4}])

def test_report_tracks_coverage_not_truth():
    record={"title":"Primary source","url":"https://science.nasa.gov/earth/facts/","accessed_at":"2026-10-28","evidence_passage":"A claim-specific passage.","scope":"Scope of evidence.","authority":5,"directness":5,"freshness":4,"relevance":5}
    storage.save_claim(valid_claim(id="supported",verdict="supported",sources=[record]))
    storage.save_claim(valid_claim(id="unknown"))
    report=storage.report()
    assert report["source_coverage"]==0.5
    assert report["claims_missing_sources"]==1

def test_claim_text_search_and_verdict_filter():
    storage.save_claim(valid_claim(text="Check the rotation period carefully."))
    assert len(storage.list_claims(search="rotation",verdict="unresolved"))==1

def test_synthetic_example_bank_validates():
    records=json.loads((Path(__file__).parents[1]/"data"/"examples.json").read_text(encoding="utf-8"))
    claims=[ClaimInput.model_validate(record) for record in records]
    assert len(claims)==7
    assert {c.verdict for c in claims}=={"supported","contradicted","unresolved","not_checkable"}
