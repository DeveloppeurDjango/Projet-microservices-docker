# Utilisation de l'image Python officielle comme base
FROM python:3.10-slim

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers nécessaires (assurez-vous d'avoir un .dockerignore approprié pour exclure les fichiers non nécessaires)
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste de l'application
COPY . .

# Commande par défaut pour exécuter l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 

