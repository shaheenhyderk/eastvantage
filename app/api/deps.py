from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session

from app.db.engine import engine


def get_db() -> Generator:
    """
    Dependency that yields a database session and ensures it is closed after use.

    Yields:
        Session: A SQLModel session connected to the database.
    """
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()


# Annotated dependency type for FastAPI to inject database sessions.
SessionDep = Annotated[Session, Depends(get_db)]
