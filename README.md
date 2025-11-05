# NICOLLIN – Gestion Temps & QSE 2025 (Python)

Démo complète basée sur **FastAPI (API)**, **Streamlit (UI)** et **SQLite (DB)**.
Fonctionne sur **GitHub Codespaces** et **Replit**.

## Démarrage rapide
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
streamlit run ui/Home.py --server.port 8501 --server.address 0.0.0.0

# Nettoyage optionnel si nécessaire
rm -rf app ui data tests README.md requirements.txt

# Création de la structure
mkdir -p app/routes app/utils ui data tests

# Fichier requirements
cat > requirements.txt << 'EOF'
fastapi==0.115.2
uvicorn==0.30.6
sqlalchemy==2.0.35
pydantic==2.9.2
python-multipart==0.0.9
passlib[bcrypt]==1.7.4
python-jose==3.3.0
apscheduler==3.10.4
pandas==2.2.2
plotly==5.24.1
streamlit==1.39.0
emails==0.6
jinja2==3.1.4
requests==2.32.3
