from typing import Optional, List
from app.db.base_class import Base
from pydantic import BaseModel

from . import episode

# Shared properties
class PurchasedEpisodeBase(BaseModel):
    pass

# Properties to receive on creation
class PurchasedEpisodeCreate(PurchasedEpisodeBase):
    pass

# Properties to receive on update
class PurchasedEpisodeUpdate(PurchasedEpisodeBase):
    pass

# Properties shared by models stored in DB
class PurchasedEpisodeInDBBase(PurchasedEpisodeBase):
    class Config:
        orm_mode = True

# Properties to return to client
class PurchasedEpisode(PurchasedEpisodeBase):
    episode: episode.Episode

# Properties properties stored in DB
class PurchasedEpisodeInDB(PurchasedEpisodeInDBBase):
    id: int
    episode_id: int
    user_id: int