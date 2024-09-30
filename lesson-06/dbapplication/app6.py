import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app = Flask(__name__, template_folder=template_dir)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)

    # Import later on
    from routes import register_routes
    register_routes(app=app, db=db)

    migrate = Migrate(app=app, db=db)
    return app
