from datetime import datetime, timezone

from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    email: EmailStr
    password_hash: str
    organisation_id: str
    is_active: bool = True
    created_at: datetime = datetime.now(timezone.utc)