# Sentiment Analysis App

Une application web pour l'analyse de sentiments de textes en utilisant des modèles de NLP (Natural Language Processing). L'application propose une interface interactive via **Gradio** et peut être déployée facilement grâce à Docker.
Lapplication est deployé sur huggingface via gradio et docker.

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

---

## ⚡ Fonctionnalités

- Analyse de sentiment (positif, négatif) pour du texte en entrée en anglais.
- Interface web interactive via **Gradio**.
- Interface web simple HTML CSS.
- Tests unitaires pour garantir la stabilité du code.
- Déploiement simple avec Docker.

---

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