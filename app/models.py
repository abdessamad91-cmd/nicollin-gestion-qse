from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True)
    nom = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    poste = Column(String, index=True)  # chauffeur, rippeur, gardien, etc.
    site = Column(String, default="")
    actif = Column(Boolean, default=True)
    role = Column(String, default="agent")  # agent, responsable, qse, admin

    pointages = relationship("Pointage", back_populates="agent")

class Pointage(Base):
    __tablename__ = "pointages"
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    jour = Column(Date, default=datetime.date.today)
    h_debut = Column(DateTime, nullable=True)
    h_fin = Column(DateTime, nullable=True)
    hdp = Column(DateTime, nullable=True)  # début pause
    hfp = Column(DateTime, nullable=True)  # fin pause
    duree_min = Column(Integer, default=0)
    pause_min = Column(Integer, default=0)
    conforme = Column(Boolean, default=True)
    note = Column(String, default="")
    agent = relationship("Agent", back_populates="pointages")

class QSERule(Base):
    __tablename__ = "qse_regles"
    id = Column(Integer, primary_key=True)
    code = Column(String, index=True)       # FIMO, FCO, ACCUEIL_SEC, AT_REACC, etc.
    libelle = Column(String)
    postes_concernes = Column(String, default="*")  # CSV de postes
    frequence_mois = Column(Integer, nullable=True) # 60 pour FIMO, 60 FCO (ex), etc.
    auto_renew = Column(Boolean, default=True)
    bloquante = Column(Boolean, default=False)
    actif = Column(Boolean, default=True)
    rappel_avant_jours = Column(Integer, default=30)

class QSEInstance(Base):
    __tablename__ = "qse_instances"
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    regle_id = Column(Integer, ForeignKey("qse_regles.id"))
    due_date = Column(Date)
    completed_date = Column(Date, nullable=True)
    status = Column(String, default="A_completer")  # A_completer, En_retard, A_verifier, Cloture
    att_provided = Column(Boolean, default=False)   # justificatif déposé ?
    att_urls = Column(String, default="")
    audit_log = Column(String, default="")
