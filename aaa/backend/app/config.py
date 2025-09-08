# config.py - environment-aware configuration
import os

class Config:
    """Configuration for Flask app.
    Use environment variables in production; defaults below are kept for local testing.
    """
    DB_USER = os.environ.get('DB_USER', 'radius')
    DB_PASS = os.environ.get('DB_PASS', 'radius')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME', 'radius')

    # Allow overriding the full SQLALCHEMY_DATABASE_URI if desired
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('SQLALCHEMY_DATABASE_URI')
        or f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secrets - change in production and keep them out of version control
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_here'
