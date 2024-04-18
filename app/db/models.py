from typing import Optional

from sqlmodel import SQLModel, Field


class AddressDB(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    street: str
    city: str
    state: str
    zip_code: str
    latitude: float
    longitude: float
