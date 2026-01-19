from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "YouLogiX"
    API_V1_STR: str = "/api/v1"
    
    # Database Settings (Loaded from .env)
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    DATABASE_URL: str
    email_address: str
    email_password: str
    # ---  Security Settings ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # This tells Pydantic to read the .env file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()