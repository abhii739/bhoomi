import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///bhoomi.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", "development-secret")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "development-jwt-secret")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173")
OPEN_METEO_BASE_URL = os.getenv("OPEN_METEO_BASE_URL", "https://api.open-meteo.com/v1")
