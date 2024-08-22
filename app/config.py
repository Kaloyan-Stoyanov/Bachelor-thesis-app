# config.py

class Config:
    SECRET_KEY = 'your_secret_key'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
