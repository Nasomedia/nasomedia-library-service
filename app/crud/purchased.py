from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Purchased
from app.schemas import PurchasedCreate, PurchasedUpdate

class CRUDPurchased(CRUDBase[Purchased, PurchasedCreate, PurchasedUpdate]):
    pass

purchased = CRUDPurchased(Purchased)