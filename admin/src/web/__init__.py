from flask import Flask, render_template
from src.web.config import config
from src.web.controllers.to_do_item import to_do_item_blueprint
from src.models.db import db, init_db


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    @app.get("/")
    def home():
        return render_template("layout.html")

    app.register_blueprint(to_do_item_blueprint)

    with app.app_context():
        init_db(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app
