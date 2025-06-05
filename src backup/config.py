import os
from dotenv import load_dotenv

# โหลด .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    DB_HOST = os.getenv("RDB_HOST")
    DB_USER = os.getenv("RDB_USER")
    DB_PASSWORD = os.getenv("RDB_PASSWORD")
    DB_NAME = os.getenv("RDB_DB")
    DB_PORT = os.getenv("RDB_PORT")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False