from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from bill_cast.db.base_class import Base


if TYPE_CHECKING:
    from .shop import Shop
    from .item import Item


class Deal(Base):
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    shop_id = Column(Integer, ForeignKey("shop.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    price_for_item = Column(Float)
    amount = Column(Float, default=1)
    price = Column(Float)

    discount = Column(Float, default=0)

    shop = relationship("Shop", back_populates="deals")
    item = relationship("Item", back_populates="deals")
