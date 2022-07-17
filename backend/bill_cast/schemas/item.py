from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    name: Optional[str]
    name_ru: Optional[str]


# Properties to receive on item creation
class ItemCreate(ItemBase):
    name: str
    name_ru: str = ""


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    unit_id: int
    name_ru: str
    tax_group_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
