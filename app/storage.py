import json, os, sqlite3, uuid
from contextlib import contextmanager
from pathlib import Path
from datetime import datetime,timezone
from app.models import ClaimInput
from dotenv import load_dotenv

load_dotenv()
DB_PATH=Path(os.getenv("DATABASE_PATH","./verification.db"))
@contextmanager
def db():
    DB_PATH.parent.mkdir(parents=True,exist_ok=True); conn=sqlite3.connect(DB_PATH);conn.row_factory=sqlite3.Row
    try:
        yield conn;conn.commit()
    except Exception:
        conn.rollback();raise
    finally: conn.close()

def initialize():
    with db() as c:
        c.executescript("""CREATE TABLE IF NOT EXISTS claims(id TEXT PRIMARY KEY,text TEXT NOT NULL,category TEXT NOT NULL,verdict TEXT NOT NULL,rationale TEXT NOT NULL,updated_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS sources(id INTEGER PRIMARY KEY AUTOINCREMENT,claim_id TEXT NOT NULL REFERENCES claims(id) ON DELETE CASCADE,title TEXT NOT NULL,url TEXT NOT NULL,accessed_at TEXT NOT NULL,evidence_passage TEXT NOT NULL,scope TEXT NOT NULL,authority INTEGER NOT NULL,directness INTEGER NOT NULL,freshness INTEGER NOT NULL,relevance INTEGER NOT NULL);""")

def save_claim(payload:ClaimInput):
    claim_id=payload.id or str(uuid.uuid4())
    with db() as c:
        c.execute("INSERT INTO claims VALUES(?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET text=excluded.text,category=excluded.category,verdict=excluded.verdict,rationale=excluded.rationale,updated_at=excluded.updated_at",
                  (claim_id,payload.text,payload.category,payload.verdict,payload.rationale,datetime.now(timezone.utc).isoformat()))
        c.execute("DELETE FROM sources WHERE claim_id=?",(claim_id,))
        for s in payload.sources:
            c.execute("INSERT INTO sources(claim_id,title,url,accessed_at,evidence_passage,scope,authority,directness,freshness,relevance) VALUES(?,?,?,?,?,?,?,?,?,?)",
                      (claim_id,s.title,str(s.url),s.accessed_at.isoformat(),s.evidence_passage,s.scope,s.authority,s.directness,s.freshness,s.relevance))
    return claim_id

def list_claims(search="",verdict=""):
    q="SELECT * FROM claims WHERE (text LIKE ? OR rationale LIKE ? OR category LIKE ?)";args=[f"%{search}%"]*3
    if verdict:q+=" AND verdict=?";args.append(verdict)
    q+=" ORDER BY updated_at DESC"
    with db() as c:
        rows=[dict(r) for r in c.execute(q,args)]
        for row in rows: row["sources"]=[dict(s) for s in c.execute("SELECT * FROM sources WHERE claim_id=? ORDER BY id",(row["id"],))]
    return rows

def report():
    claims=list_claims();total=len(claims);counts={}
    for c in claims: counts[c["verdict"]]=counts.get(c["verdict"],0)+1
    missing=sum(not c["sources"] for c in claims)
    return {"claim_count":total,"verdict_counts":counts,"source_coverage":round((total-missing)/total,3) if total else None,
            "claims_missing_sources":missing,"limitations":"A stored verdict is a reviewer judgment, not automated fact verification. Unresolved does not mean false."}

def seed_if_empty(path="data/examples.json"):
    if list_claims(): return
    records=json.loads(Path(path).read_text(encoding="utf-8"))
    for record in records: save_claim(ClaimInput.model_validate(record))
