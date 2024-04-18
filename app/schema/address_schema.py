from typing import Optional

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    latitude: float
    longitude: float
