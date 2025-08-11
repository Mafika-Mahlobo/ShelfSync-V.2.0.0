from flask import Flask
from app.routes.user_routes import user_routesbp

def create_app():

    app = Flask(__name__)

    app.register_blueprint(user_routesbp)
    
    return app