import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app = Flask(__name__, template_folder=template_dir)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"

    app.secret_key = "THIS IS SECRET"

    db.init_app(app=app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for("home"))
    
    bcrypt = Bcrypt(app=app)

    # Import later on
    from routes import register_routes
    register_routes(app=app, db=db, bcrypt=bcrypt)

    migrate = Migrate(app=app, db=db)
    return app
