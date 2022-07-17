from pydantic import BaseModel


# Shared properties
class UnitBase(BaseModel):
    name: str


# Properties to receive on item creation
class UnitCreate(UnitBase):
    pass


# Properties to receive on item update
class UnitUpdate(UnitBase):
    pass


# Properties shared by models stored in DB
class UnitInDBBase(UnitBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Unit(UnitInDBBase):
    pass


# Properties properties stored in DB
class UnitInDB(UnitInDBBase):
    pass
