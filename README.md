# 📊 Sentiment Analysis App

Une application web pour l'analyse de sentiments de textes en utilisant le modèle distilbert-base-uncased-finetuned-sst-2-english. L'application propose également une interface interactive via **Gradio** et peut être déployée facilement grâce à **Docker**.
Lapplication est deployé sur **huggingface spaces** via gradio et docker.

![Python](https://img.shields.io/badge/python-3.12.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688?logo=fastapi)
![Gradio](https://img.shields.io/badge/Gradio-5.43.1-orange)
![Docker](https://img.shields.io/badge/Docker-28.3.2-blue?logo=docker)

---

## 📑 Table des matières
- [Structure du projet](#-structure-du-projet)
- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Liens](#-liens)
- [Résultat du mini benchmark](#résultat-du-mini-benchmark)
---


## 📂 Structure du projet

- `app.py` : Fichier principal de l'application FastAPI.
- `gradio_app/` : Interface utilisateur Gradio pour tester l'analyse de sentiments.
- `static/` : Fichiers CSS, JS et images statiques.
- `templates/` : Modèles HTML pour l'application web.
- `test/` : Tests unitaires avec `pytest`.
- `benchmark.py` : Script pour comparer entre différents modèles.
- `requirements.txt` : Dépendances Python nécessaires.
- `Dockerfile` : Fichier pour créer une image Docker de l'application.
- `tests_swagger.docx`:  Captures d’écran : Swagger (/docs) et page HTML de test.

---

## ⚡ Fonctionnalités

- Analyse de sentiment (positif, négatif) pour du texte en entrée en anglais.
- API REST avec **FastAPI**.
- Interface web simple **HTML CSS**.
- Interface web interactive via **Gradio**.
- Tests unitaires **pytest** pour garantir la stabilité du code et **yml** visible sur github.
- Déploiement simple avec **Docker**.

---


## 🛠 Installation

Clonez le projet :

```bash
git clone https://github.com/sara-git-hub/sentimentanalysis.git
cd sentimentanalysis
```

Créez un environnement virtuel et installez les dépendances :

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Lancez FastAPI :

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 7860
```

➡ Application disponible sur : http://127.0.0.1:7860

Avec Docker :

```bash
docker build -t sentiment-app .
docker run -d --name sentiment-container -p 7860:7860 sentiment-app
```
---

## 💻 Utilisation

Exemple API FastAPI

```bash
curl -X 'POST' \
  'http://127.0.0.1:7860/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "I am happy"
}'
```
Réponse :

```bash
{
  "text": "I am happy",
  "sentiment": "positive",
  "confidence": 1
}
```

## 🚀 Liens

- Application gradio sur huggingface: https://huggingface.co/spaces/Sarahugg/app_sentiment
- Application docker sur huggingface: https://huggingface.co/spaces/Sarahugg/sentiment_app
- Lien Jira                         : https://sarabouabid.atlassian.net/jira/software/projects/SA/boards/199 

## Résultat du mini benchmark

|                                                       |Modèle  Latence (ms)       |Accuracy (%)
|-------------------------------------------------------|---------------------------|--------------
|distilbert-base-uncased-finetuned-sst-2-english        |265.05                     |100.0
|**cardiffnlp/twitter-roberta-base-sentiment-latest**   |97.01                      |100.0
|         siebert/sentiment-roberta-large-english       |486.43                     |100.0
