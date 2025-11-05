from fastapi import FastAPI
app = FastAPI(title="NICOLLIN - QSE API de base")

@app.get("/")
def root():
    return {"ok": True, "message": "API prête - NICOLLIN QSE 2025"}
