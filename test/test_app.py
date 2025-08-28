import sys
import os
from fastapi.testclient import TestClient
from app import app

# ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#crée un client de test simulé pour l'application FastAPI
client = TestClient(app)

# -----------------------------
# Tests pour le POST JSON
# -----------------------------
def test_analyze_positive():
    response = client.post("/", json={"text": "I love this product"})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] in ["positive", "negative"]
    assert 0 <= data["confidence"] <= 1

def test_analyze_negative():
    response = client.post("/", json={"text": "I hate this product"})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] in ["positive", "negative"]
    assert 0 <= data["confidence"] <= 1

def test_analyze_empty_text():
    response = client.post("/", json={"text": ""})
    # Validation Pydantic avec min_length=1 → 422
    assert response.status_code == 422

def test_analyze_missing_text():
    response = client.post("/", json={})
    # JSON invalide → 422
    assert response.status_code == 422

# -----------------------------
# Test pour la page HTML
# -----------------------------
def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

# -----------------------------
# Test de performance simple
# -----------------------------
def test_response_time():
    import time
    start = time.time()
    response = client.post("/", json={"text": "Quick test"})
    end = time.time()
    assert response.status_code == 200
    assert (end - start) < 2  # réponse en moins de 2 secondes

# -----------------------------
# Test health
# -----------------------------

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"