from flask import Flask

from app.app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


application, db, migrate = create_app()


if __name__ == "__main__":
    application.run(load_dotenv=True)
