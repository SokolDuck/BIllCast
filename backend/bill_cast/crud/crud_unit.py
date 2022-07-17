from typing import Optional
from sqlalchemy.orm import Session

from bill_cast.crud.base import CRUDBase
from bill_cast.models.unit import Unit
from bill_cast.schemas.unit import UnitCreate, UnitUpdate


class CRUDUnit(CRUDBase[Unit, UnitCreate, UnitUpdate]):
    def get_by_name(self, db: Session, name: str) -> Optional[Unit]:
        return db.query(Unit).filter(Unit.name == name).first()


unit = CRUDUnit(Unit)
