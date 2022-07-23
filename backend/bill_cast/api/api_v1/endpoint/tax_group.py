from typing import Any, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from bill_cast import schemas, crud, models
from bill_cast.api import deps


router = APIRouter()


@router.get("/", response_model=List[schemas.TaxGroup])
def read_tax_group(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    units = crud.tax_group.get_multi(db, skip=skip, limit=limit)
    return units


@router.post("/", response_model=schemas.TaxGroup)
def create_tax_group(
    *,
    db: Session = Depends(deps.get_db),
    obj_create: schemas.TaxGroupCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create new unit.
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=405,
            detail="Only superuser can create new Tax Group"
        )
    tax_group = crud.tax_group.get_by_name(db, name=obj_create.name)

    if tax_group:
        raise HTTPException(
            status_code=400,
            detail="The tax group with this name already exists in the system.",
        )
    else:
        tax_group = crud.tax_group.create(db, obj_in=obj_create)
    
    return tax_group
