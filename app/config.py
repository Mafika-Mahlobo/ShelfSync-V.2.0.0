import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMy_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_URI')

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_URI')

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_URI')
    TESTING = True
