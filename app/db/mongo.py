from pymongo import MongoClient

from app.config.settings import settings

client = MongoClient(
    settings.MONGO_URI,
    serverSelectionTimeoutMS=5000,
)


def get_organisation_database(organisation_id: str):
    organisation_id = organisation_id.strip().lower()

    if not organisation_id:
        raise ValueError("Organisation ID is required")

    database_name = f"reckomate_{organisation_id}"
    return client[database_name]


def check_mongodb_connection() -> bool:
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False