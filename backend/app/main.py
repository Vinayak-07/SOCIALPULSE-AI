from fastapi import FastAPI
from backend.app.db.database import init_db
from backend.app.demo.demo_data_generator import generate

app = FastAPI(title="SocialPulse AI")

@app.on_event("startup")
async def startup():
    init_db()

@app.get("/health")
def health(): return {"status":"ok","mode":"DEMO"}

@app.get("/api/v1/system/status")
def status(): return {"mode":"DEMO","data_mode":"DEMO","note":"Analytical indicators only; not verified threats."}

@app.post("/api/v1/demo/seed")
def seed():
    n = generate()
    return {"seeded":n,"mode":"DEMO"}
