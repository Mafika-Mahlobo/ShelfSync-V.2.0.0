import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMy_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_URI')

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_URI')

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_URI')
