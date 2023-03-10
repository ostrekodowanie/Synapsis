from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    DB_HOST: str
    DB_PASSWORD: str
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    class Config:
        env_file = ".env"

settings = Settings()