from flask import Flask, redirect, render_template
from src.web.config import config
from src.web.controllers.category import category_blueprint
from src.web.controllers.frecuent_task import frecuent_task_blueprint
from src.web.controllers.regular_task import regular_task_blueprint
from src.models.db import db, init_db


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    @app.get("/")
    def home():
        return render_template("layout.html")
        # return redirect("/categories/all")

    app.register_blueprint(category_blueprint)
    app.register_blueprint(frecuent_task_blueprint)
    app.register_blueprint(regular_task_blueprint)

    with app.app_context():
        init_db(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app
