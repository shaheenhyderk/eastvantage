from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session

from app.db.engine import engine


def get_db() -> Generator:
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()


SessionDep = Annotated[Session, Depends(get_db)]
