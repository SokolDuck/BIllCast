from typing import Optional

from datetime import date

from pydantic import BaseModel


# Shared properties
class DealBase(BaseModel):
    data: Optional[date]
    price_for_item: Optional[float]
    amount: Optional[float]
    price: Optional[float]

    discount: Optional[float]


# Properties to receive on item creation
class DealCreate(DealBase):
    data: date
    price_for_item: float
    amount: float
    price: float


# Properties to receive on item update
class DealUpdate(DealBase):
    pass


# Properties shared by models stored in DB
class DealInDBBase(DealBase):
    id: int
    shop_id: int
    item_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Deal(DealInDBBase):
    pass


# Properties properties stored in DB
class DealInDB(DealInDBBase):
    pass
