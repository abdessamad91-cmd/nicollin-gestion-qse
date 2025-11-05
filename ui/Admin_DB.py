import streamlit as st
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

st.title("Admin DB – Synthèse")
db: Session = SessionLocal()
try:
    st.metric("Agents", db.query(models.Agent).count())
    st.metric("Pointages", db.query(models.Pointage).count())
    st.metric("Règles QSE", db.query(models.QSERule).count())
    st.metric("Exigences en cours", db.query(models.QSEInstance).count())
finally:
    db.close()
