import os

from dotenv import load_dotenv

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(ROOT_DIR, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    POKEAPI_URL = "https://pokeapi.co/api/v2/"
    RQ_REDIS_URL = "redis://redis:6379/0"
    RQ_DASHBOARD_REDIS_URL = "redis://redis:6379/0"
    RQ_SCHEDULER_INTERVAL = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(ROOT_DIR, "app.sqlite"),
    )
