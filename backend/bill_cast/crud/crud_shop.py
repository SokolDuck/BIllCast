from typing import Optional

from sqlalchemy.orm import Session

from bill_cast.crud.base import CRUDBase
from bill_cast.models.shop import Shop
from bill_cast.schemas.shop import ShopCreate, ShopUpdate


class CRUDShop(CRUDBase[Shop, ShopCreate, ShopUpdate]):
    def get_by_name(self, db: Session, name: str) -> Optional[Shop]:
        return db.query(Shop).filter(Shop.name == name).first()


shop = CRUDShop(Shop)
