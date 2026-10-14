from fastapi import APIRouter, HTTPException

from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    return login_user(
        email=str(payload.email).lower(),
        organisation_id=payload.organisation_id,
        password=payload.password,
    )