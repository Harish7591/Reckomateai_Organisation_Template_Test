from fastapi import HTTPException, status
from pymongo.errors import PyMongoError

from app.db.mongo import get_organisation_database
from app.utils.security import (
    create_access_token,
    verify_password,
)


def login_user(
    email: str,
    organisation_id: str,
    password: str,
) -> dict:
    try:
        database = get_organisation_database(organisation_id)

        user = database["users"].find_one({
            "email": email.lower(),
            "organisation_id": organisation_id,
        })

        if not user or not user.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email, organisation ID, or password",
            )

        if not verify_password(
            password,
            user.get("password_hash", ""),
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email, organisation ID, or password",
            )

        token = create_access_token(
            subject=str(user["_id"]),
            organisation_id=organisation_id,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Organisation database unavailable",
        )