# Import all the models, so that Base has them before being
# imported by Alembic
from bill_cast.db.base_class import Base
from bill_cast.models.tax_group import TaxGroup
from bill_cast.models.unit import Unit
from bill_cast.models.item import Item
from bill_cast.models.shop import Shop
from bill_cast.models.deal import Deal
from bill_cast.models.user import User
