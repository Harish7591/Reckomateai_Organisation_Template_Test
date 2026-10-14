import os

from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = FastAPI(title="Organisation Backend", version="1.0.0")


@app.get("/")
def home():
    return {
        "message": "Organisation backend is running",
        "status": "healthy",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/health/db")
def database_health_check():
    mongo_uri = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017",
    )
    database_name = os.getenv(
        "MONGO_DATABASE",
        "organisation_db",
    )

    try:
        client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=3000,
        )
        client.admin.command("ping")
        client.close()

        return {
            "status": "healthy",
            "database": database_name,
        }
    except PyMongoError:
        return {
            "status": "unhealthy",
            "database": database_name,
        }