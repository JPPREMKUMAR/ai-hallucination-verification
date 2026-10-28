from fastapi import FastAPI,HTTPException,Query
from app.models import ClaimImport,ClaimInput
from app import storage

app=FastAPI(title="Hallucination Detection and Research Verification",version="0.1.0",
            description="Claim-level evidence workspace; verdicts are human-entered and never inferred from missing sources.")
storage.initialize()
storage.seed_if_empty()

@app.get("/api/health")
def health(): return {"status":"ok"}

@app.get("/api/claims")
def claims(search:str="",verdict:str=""): return storage.list_claims(search,verdict)

@app.post("/api/claims",status_code=201)
def create_claim(payload:ClaimInput):
    claim_id=storage.save_claim(payload);return {"id":claim_id,"saved":True}

@app.post("/api/claims/import",status_code=201)
def import_claims(payload:ClaimImport):
    ids=[storage.save_claim(c) for c in payload.claims];return {"imported":len(ids),"ids":ids}

@app.put("/api/claims/{claim_id}")
def update_claim(claim_id:str,payload:ClaimInput):
    if not any(row["id"]==claim_id for row in storage.list_claims()): raise HTTPException(404,"Claim not found")
    updated=payload.model_copy(update={"id":claim_id});storage.save_claim(updated);return {"updated":True,"id":claim_id}

@app.get("/api/report")
def get_report(): return storage.report()
