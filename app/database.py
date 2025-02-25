import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client.store_database
collection = db.products
