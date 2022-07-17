from typing import Optional


from pydantic import BaseModel


# Shared properties
class TaxGroupBase(BaseModel):
    name: Optional[str]
    tax_value: Optional[int]


# Properties to receive on item creation
class TaxGroupCreate(TaxGroupBase):
    name: str
    tax_value: int = 0


# Properties to receive on item update
class TaxGroupUpdate(TaxGroupBase):
    pass


# Properties shared by models stored in DB
class TaxGroupInDBBase(TaxGroupBase):
    id: int
    name: str
    tax_value: int

    class Config:
        orm_mode = True


# Properties to return to client
class TaxGroup(TaxGroupInDBBase):
    pass


# Properties properties stored in DB
class TaxGroupInDB(TaxGroupInDBBase):
    pass
