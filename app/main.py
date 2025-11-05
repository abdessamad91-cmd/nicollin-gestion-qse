from fastapi import FastAPI
from .database import Base, engine
from . import models

app = FastAPI(title="NICOLLIN – API QSE & Temps")

# Crée les tables si absentes
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"ok": True, "message": "API prête - NICOLLIN QSE 2025"}
