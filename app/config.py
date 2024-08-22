# config.py

class Config:
    # Base configuration
    SECRET_KEY = 'your_secret_key'
    # Other configurations...

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # Add other test-specific configurations...