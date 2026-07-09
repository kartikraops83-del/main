import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///railway_tracker.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# API Configuration
RAILWAY_API_CONFIG = {
    'BASE_URL': 'https://railwayapi.com/v2/',
    'API_KEY': os.getenv('RAILWAY_API_KEY', ''),
    'TIMEOUT': 10,
    'RATE_LIMIT': 1000  # requests per day
}

IRCTC_CONFIG = {
    'BASE_URL': 'https://www.irctc.co.in/api/',
    'TIMEOUT': 15,
    'RATE_LIMIT': 500
}

# Cache Configuration
CACHE_TYPE = 'redis'
CACHE_REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
CACHE_DEFAULT_TIMEOUT = 300

# Database Configuration
DB_UPDATE_INTERVAL = 300  # seconds (5 minutes)
