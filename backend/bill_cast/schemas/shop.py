from typing import Optional

from pydantic import BaseModel


# Shared properties
class ShopBase(BaseModel):
    name: Optional[str]
    address: Optional[str]


# Properties to receive on item creation
class ShopCreate(ShopBase):
    name: str


# Properties to receive on item update
class ShopUpdate(ShopBase):
    pass


# Properties shared by models stored in DB
class ShopInDBBase(ShopBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Shop(ShopInDBBase):
    pass


# Properties properties stored in DB
class ShopInDB(ShopInDBBase):
    pass
