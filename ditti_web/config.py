from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', False)
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
