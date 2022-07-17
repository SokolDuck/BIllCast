from typing import Optional
from sqlalchemy.orm import Session

from bill_cast import models
from bill_cast import schemas


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate, unit_id: int, tax_group_id: int):
    db_item = models.Item(
        **item.dict(),
        tax_group_id=tax_group_id,
        unit_id=unit_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_tax_group(db: Session, *, id: Optional[int] = None, name: Optional[str] = None):
    queryset = db.query(models.TaxGroup)

    if id is not None:
        queryset = queryset.filter(models.TaxGroup.id == id)
    if name is not None:
        queryset = queryset.filter(models.TaxGroup.name == name.upper())

    return queryset.first()

def create_tax_group(db: Session, tax_group: schemas.TaxGroupCreate):
    db_tax_group = models.TaxGroup(
        name=tax_group.name,
        tax_value=tax_group.tax_value
    )
    db.add(db_tax_group)
    db.commit()
    db.refresh(db_tax_group)
    return db_tax_group

def get_unit(db: Session, id: int):
    return db.query(models.Unit).filter(models.Unit.id == id).first()

def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unit).offset(skip).limit(limit).all()

def create_unit(db: Session, unit: schemas.UnitCreate):
    db_unit = models.Unit(
        name=unit.name
    )
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

def get_shop(db: Session, shop_id: int):
    return db.query(models.Shop).filter(models.Shop.id == shop_id).first()

def create_shop(db: Session, shop: schemas.ShopCreate):
    db_shop = models.Shop(
        **shop.dict()
    )
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop

def get_deal(db: Session, deal_id: int):
    return db.query(models.Deal).filter(models.Deal.id == deal_id).first()

def get_deals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Deal).offset(skip).limit(limit).all()

def create_deal(db: Session, deal: schemas.DealCreate, shop_id: int, item_id: int):
    db_deal = models.Deal(
        **deal.dict(),
        shop_id=shop_id,
        item_id=item_id
    )
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal
