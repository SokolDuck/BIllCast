from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from bill_cast.db.base_class import Base


if TYPE_CHECKING:
    from .item import Item


class TaxGroup(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    tax_value = Column(Integer, unique=True)

    items = relationship("Item", back_populates="tax_group")
