from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from bill_cast.db.base_class import Base


if TYPE_CHECKING:
    from .tax_group import TaxGroup
    from .unit import Unit
    from .deal import Deal
    from .user import User


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    name_ru = Column(String, unique=True, index=True)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    tax_group_id = Column(Integer, ForeignKey("taxgroup.id"))
    user_id = Column(Integer, ForeignKey("user.id"), index=True)

    unit = relationship("Unit", back_populates="items")
    deals = relationship("Deal", back_populates="item")
    tax_group = relationship("TaxGroup", back_populates="items")
    user = relationship("User", back_populates="items")
