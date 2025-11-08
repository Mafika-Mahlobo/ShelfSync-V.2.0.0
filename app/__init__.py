from flask import Flask
from app.routes.user_routes import user_routesbp
from app.routes.book_routes import booksbp
from app.routes.library_routes import librarybp
from app.routes.transaction_routes import check_inbp, check_outbp

def create_app():

    app = Flask(__name__)

    app.register_blueprint(user_routesbp)
    app.register_blueprint(booksbp)
    app.register_blueprint(librarybp)
    app.register_blueprint(check_outbp)
    
    return app