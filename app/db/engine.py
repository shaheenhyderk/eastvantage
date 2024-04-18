from sqlalchemy import create_engine
from sqlmodel import SQLModel

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
