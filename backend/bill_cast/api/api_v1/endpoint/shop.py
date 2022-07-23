from typing import Any, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from bill_cast import schemas, crud, models
from bill_cast.api import deps


router = APIRouter()


@router.get("/", response_model=List[schemas.Shop])
def read_shop(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    units = crud.shop.get_multi(db, skip=skip, limit=limit)
    return units


@router.post("/", response_model=schemas.Shop)
def create_shop(
    *,
    db: Session = Depends(deps.get_db),
    obj_create: schemas.ShopCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create new unit.
    """
    
    shop = crud.shop.get_by_name(db, name=obj_create.name)

    if shop:
        raise HTTPException(
            status_code=400,
            detail="The shop with this name already exists in the system.",
        )
    else:
        shop = crud.shop.create(db, obj_in=obj_create)
    
    return shop
