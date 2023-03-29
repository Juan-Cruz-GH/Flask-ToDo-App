from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    db.create_all()
    config_db(app)


def config_db(app):
    @app.before_first_request
    def init_database():
        db.create_all()
