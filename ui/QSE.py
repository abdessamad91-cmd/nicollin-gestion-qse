import streamlit as st
from datetime import date, timedelta
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

st.title("QSE – Exigences (démo)")

db: Session = SessionLocal()

agents = db.query(models.Agent).all()
choices_a = {f"{a.nom} ({a.poste})": a.id for a in agents}
regles = db.query(models.QSERule).filter(models.QSERule.actif==True).all()
choices_r = {f"{r.code} – {r.libelle}": r.id for r in regles}

st.subheader("Créer une nouvelle exigence")
col1, col2 = st.columns(2)
with col1:
    agent_id = st.selectbox("Agent", list(choices_a.keys()))
with col2:
    regle_id = st.selectbox("Règle", list(choices_r.keys()))
due = st.date_input("Échéance", date.today()+timedelta(days=30))
if st.button("Créer"):
    inst = models.QSEInstance(agent_id=choices_a[agent_id], regle_id=choices_r[regle_id], due_date=due, status="A_completer")
    db.add(inst); db.commit()
    st.success(f"Instance créée (ID {inst.id})")

st.subheader("Exigences en cours")
insts = db.query(models.QSEInstance).order_by(models.QSEInstance.id.desc()).limit(20).all()
for i in insts:
    st.write(f"ID {i.id} – agent {i.agent_id} – règle {i.regle_id} – due {i.due_date} – statut {i.status}")
    if st.button(f"Clôturer {i.id}", key=f"cl_{i.id}"):
        i.status="Cloture"; i.completed_date=date.today()
        # auto-renouvellement si fréquence définie
        r = db.get(models.QSERule, i.regle_id)
        if r and r.frequence_mois:
            next_due = date.today() + timedelta(days=r.frequence_mois*30)
            db.add(models.QSEInstance(agent_id=i.agent_id, regle_id=i.regle_id, due_date=next_due, status="A_completer"))
        db.commit()
        st.success("Clôturé (et replanifié si périodique).")

db.close()
