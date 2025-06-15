import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Base configuration
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Health Perks API"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://health-perks-bot.lovable.app",  # Production frontend URL
        os.getenv("FRONTEND_URL", "")  # Railway frontend URL
    ]
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./health_perks.db")
    
    # SSL/TLS
    SSL_CERTIFICATE: str = os.getenv("SSL_CERTIFICATE", "")
    SSL_KEY: str = os.getenv("SSL_KEY", "")
    
    # Railway specific
    PORT: int = int(os.getenv("PORT", "8000"))
    RAILWAY_STATIC_URL: str = os.getenv("RAILWAY_STATIC_URL", "")
    
    class Config:
        case_sensitive = True

settings = Settings() 