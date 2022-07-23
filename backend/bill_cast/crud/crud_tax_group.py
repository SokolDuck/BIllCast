from typing import Optional

from sqlalchemy.orm import Session

from bill_cast.crud.base import CRUDBase
from bill_cast.models.tax_group import TaxGroup
from bill_cast.schemas.tax_group import TaxGroupCreate, TaxGroupUpdate


class CRUDTaxGroup(CRUDBase[TaxGroup, TaxGroupCreate, TaxGroupUpdate]):
    def get_by_name(self, db: Session, name: str) -> Optional[TaxGroup]:
        return db.query(TaxGroup).filter(TaxGroup.name == name).first()


tax_group = CRUDTaxGroup(TaxGroup)
