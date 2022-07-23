from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from bill_cast.db.base_class import Base


if TYPE_CHECKING:
    from .item import Item
    from .user import User


class Unit(Base):
    __table_args__ = (
        UniqueConstraint('user_id', 'name'),
    )
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)

    items = relationship("Item", back_populates="unit")
    user = relationship("User", back_populates="units")
