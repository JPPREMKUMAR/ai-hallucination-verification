from datetime import date
from typing import Literal
from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator

Verdict=Literal["supported","contradicted","unresolved","not_checkable"]

class SourceInput(BaseModel):
    title: str = Field(min_length=1,max_length=300)
    url: HttpUrl
    accessed_at: date
    evidence_passage: str = Field(min_length=1,max_length=4000)
    scope: str = Field(min_length=1,max_length=1000)
    authority: int = Field(ge=1,le=5)
    directness: int = Field(ge=1,le=5)
    freshness: int = Field(ge=1,le=5)
    relevance: int = Field(ge=1,le=5)

class ClaimInput(BaseModel):
    id: str | None = Field(default=None,min_length=1,max_length=100)
    text: str = Field(min_length=5,max_length=3000)
    category: str = Field(default="general",max_length=100)
    verdict: Verdict
    rationale: str = Field(min_length=10,max_length=4000)
    sources: list[SourceInput] = Field(default_factory=list,max_length=20)

    @field_validator("rationale")
    @classmethod
    def no_blank_rationale(cls,value):
        if not value.strip(): raise ValueError("A rationale is required")
        return value.strip()

    @model_validator(mode="after")
    def supported_verdict_needs_evidence(self):
        if self.verdict in {"supported","contradicted"} and not self.sources:
            raise ValueError("Supported and contradicted verdicts require evidence sources")
        return self

class ClaimImport(BaseModel):
    claims: list[ClaimInput] = Field(min_length=1,max_length=1000)
