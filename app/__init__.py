from flask import Flask
from app.routes.user_routes import user_routesbp, user_deletebp
from app.routes.book_routes import booksbp, book_searchbp
from app.routes.library_routes import librarybp, library_deletebp, library_getbp, library_searchbp, library_editbp
from app.routes.transaction_routes import check_inbp, check_outbp

def create_app():

    app = Flask(__name__)

    app.register_blueprint(user_routesbp)
    app.register_blueprint(booksbp)
    app.register_blueprint(librarybp)
    app.register_blueprint(check_outbp)
    app.register_blueprint(book_searchbp)
    app.register_blueprint(library_deletebp)
    app.register_blueprint(user_deletebp)
    app.register_blueprint(library_getbp)
    app.register_blueprint(library_searchbp)
    app.register_blueprint(library_editbp)
    
    return app