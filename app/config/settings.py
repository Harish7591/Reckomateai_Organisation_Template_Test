import os


class Settings:
    APP_NAME: str = "Organisation Backend"
    MONGO_URI: str = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017",
    )
    JWT_SECRET_KEY: str = os.getenv(
        "JWT_SECRET_KEY",
        "local-development-secret-change-me",
    )
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()