from typing import Optional, List
from app.db.base_class import Base
from pydantic import BaseModel

from . import episode

# Shared properties
class PurchasedBase(BaseModel):
    pass

# Properties to receive on creation
class PurchasedCreate(PurchasedBase):
    pass

# Properties to receive on update
class PurchasedUpdate(PurchasedBase):
    pass

# Properties shared by models stored in DB
class PurchasedInDBBase(PurchasedBase):
    class Config:
        orm_mode = True

# Properties to return to client
class Purchased(PurchasedInDBBase):
    pass

# Properties properties stored in DB
class PurchasedInDB(PurchasedInDBBase):
    id: int
    episode_id: int
    user_id: int