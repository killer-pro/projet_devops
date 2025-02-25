# Utilisation de l'image Python officielle
FROM python:3.9-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /code

# Copier les fichiers nécessaires
COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY ./app /code/app

# Exposer le port sur lequel l'API tourne
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
