import streamlit as st
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

st.title("Agents – Gestion")
db: Session = SessionLocal()

with st.form("add_agent"):
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    poste = st.selectbox("Poste", ["chauffeur","chauffeur_grue","rippeur","gardien","volant"])
    site = st.text_input("Site", "NANCY")
    submitted = st.form_submit_button("Ajouter")
    if submitted and nom and email:
        a = models.Agent(nom=nom, email=email, poste=poste, site=site)
        db.add(a); db.commit()
        st.success("Agent ajouté.")

st.subheader("Liste")
rows = db.query(models.Agent).all()
for a in rows:
    st.write(f"• {a.id} – {a.nom} – {a.poste} – {a.site} – actif={a.actif}")

db.close()
