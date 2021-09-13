from flask import Flask
from flask_migrate import Migrate
from flask_rq2 import RQ
from flask_sqlalchemy import SQLAlchemy
import rq_dashboard

from config import Config

rq = RQ()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    rq.init_app(app)

    from app import api

    app.register_blueprint(api.bp)

    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")
    return app


from app import models
