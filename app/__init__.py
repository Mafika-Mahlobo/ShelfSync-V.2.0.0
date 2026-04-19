from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig

db = SQLAlchemy()

config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

def create_app(config_name='development'):
    app = Flask(__name__)

    config_class = config_map.get(config_name, DevelopmentConfig)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes.user.auth.register import users

    app.register_blueprint(users)
    
    return app