from typing import Optional, List
from pydantic import BaseModel
from . import series

# Shared properties
class LikedBase(BaseModel):
    pass

# Properties to receive on creation
class LikedCreate(LikedBase):
    pass

# Properties to receive on update
class LikedUpdate(LikedBase):
    pass

# Properties shared by models stored in DB
class LikedInDBBase(LikedBase):
    class Config:
        orm_mode = True

# Properties to return to client
class Liked(LikedInDBBase):
    pass

# Properties properties stored in DB
class LikedInDB(LikedInDBBase):
    id: int
    user_id: int
    series_id: int