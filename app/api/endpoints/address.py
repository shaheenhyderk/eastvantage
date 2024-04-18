from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from app.api.deps import SessionDep
from app.db.models import AddressDB
from app.schema.address_schema import Address
from app.utils.distance_util import DistanceUtil

router = APIRouter()


@router.post("/create/", response_model=Address, status_code=status.HTTP_201_CREATED)
async def create_address(address: Address, db: SessionDep):
    """Creates a new address record."""
    db_address = AddressDB(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


@router.get("/list/", response_model=List[Address])
async def read_addresses(db: SessionDep):
    """Returns all address records."""
    return db.query(AddressDB).all()


@router.get("/get/{address_id}", response_model=Address)
async def read_address(address_id: int, db: SessionDep):
    """Returns a specific address by its ID or raises HTTPException if not found."""
    address = db.get(AddressDB, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.put("/update/{address_id}", response_model=Address)
async def update_address(address_id: int, update_data: Address, db: SessionDep):
    """Updates an existing address by ID."""
    address = db.get(AddressDB, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    address_data = update_data.dict(exclude_unset=True)
    for key, value in address_data.items():
        setattr(address, key, value)
    db.commit()
    return address


@router.delete("/delete/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(address_id: int, db: SessionDep):
    """Deletes an address by its ID or raises HTTPException if not found."""
    address = db.get(AddressDB, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(address)
    db.commit()
    return {}


@router.get("/search/", response_model=List[Address])
async def find_addresses_within_km(latitude: float, longitude: float, km: float, db: SessionDep):
    """Finds addresses within a specified distance from a given coordinate."""
    addresses = db.query(AddressDB).all()
    coordinate = (latitude, longitude)
    result = [address for address in addresses if DistanceUtil.is_within_range(address, coordinate, km)]
    return result
