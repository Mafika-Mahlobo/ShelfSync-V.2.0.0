import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.config['SQLALCHEMy_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    #app.register_blueprint()
    
    return app