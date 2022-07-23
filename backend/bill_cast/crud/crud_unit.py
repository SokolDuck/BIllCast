import logging
from typing import List, Optional
from sqlalchemy.orm import Session

from bill_cast.crud.base import CRUDBase
from bill_cast.models.unit import Unit
from bill_cast.schemas.unit import UnitCreate, UnitUpdate


logger = logging.getLogger(__name__)

class CRUDUnit(CRUDBase[Unit, UnitCreate, UnitUpdate]):
    def get_by_name(self, db: Session, name: str) -> Optional[Unit]:
        return db.query(Unit).filter(Unit.name == name).first()

    def create(self, db: Session, *, obj_in: UnitCreate, user_id: int) -> Unit:
        return super().create(db, obj_in=obj_in, user_id=user_id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100, user_id: int) -> List[Unit]:
        return db.query(self.model).filter(Unit.user_id == user_id).offset(skip).limit(limit).all()


unit = CRUDUnit(Unit)
