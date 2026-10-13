import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from backend/.env
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "HR AI Agent Backend")
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ["true", "1", "t"]
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    # AI
    AI_PROVIDER: str = os.getenv("AI_PROVIDER")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    
    # Email
    EMAIL_HOST: str = os.getenv("EMAIL_HOST")
    EMAIL_PORT: int = int(os.getenv("EMAIL_PORT", 587))
    EMAIL_USERNAME: str = os.getenv("EMAIL_USERNAME")
    EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

settings = Settings()
