from .crud_user import user
from .crud_unit import unit
from .crud_tax_group import tax_group
from .crud_shop import shop

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
