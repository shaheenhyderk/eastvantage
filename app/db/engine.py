from sqlalchemy import create_engine
from sqlmodel import SQLModel

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)


def create_db_and_tables():
    """
    Creates database tables based on SQLModel metadata definitions.

    This function initializes the database by creating all tables defined in the SQLModel metadata.
    It uses the engine configured with settings from the application's configuration. This function should
    be called at application startup to ensure all necessary database tables exist.

    Note: This method is not ideal for large-scale applications where frequent schema alterations occur,
    as it may lead to performance bottlenecks and difficulties in managing database migrations.
    """
    SQLModel.metadata.create_all(engine)
