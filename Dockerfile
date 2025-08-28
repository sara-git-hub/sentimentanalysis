# Utiliser une image Python légère
FROM python:3.12-slim

# Définir le répertoire de travail à l’intérieur du conteneur
WORKDIR /app

# ----------------------------
# Installer les dépendances système nécessaires :
# - build-essential : compilation de paquets (C, C++)
# - python3-dev     : headers Python pour compiler certains modules
# - git             : utile pour cloner ou installer depuis GitHub
# Puis on nettoie le cache apt pour réduire la taille de l’image
# ----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------
# Configuration du cache Hugging Face
# - HF_HOME : répertoire local du cache
# - HF_HUB_DISABLE_SYMLINKS_WARNING : éviter les warnings liés aux symlinks
# On crée le dossier et on donne tous les droits (777) 
# pour éviter les problèmes de permissions dans Docker
# ----------------------------
ENV HF_HOME=/app/.cache/huggingface
ENV HF_HUB_DISABLE_SYMLINKS_WARNING=1
RUN mkdir -p $HF_HOME && chmod -R 777 $HF_HOME

# ----------------------------
# Installer les dépendances Python
# On commence par copier requirements.txt 
# puis on installe Torch (version CPU uniquement, plus léger)
# et enfin toutes les autres dépendances listées dans requirements.txt
# ----------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir torch==2.8.0+cpu --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source dans /app
COPY . .

# Exposer le port 7860 
EXPOSE 7860

# ----------------------------
# Commande de démarrage du serveur
# - uvicorn lance l’application FastAPI
# - app:app → correspond à "app.py" et à l’instance "app"
# - écoute sur toutes les IPs du conteneur (--host 0.0.0.0)
# ----------------------------
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
