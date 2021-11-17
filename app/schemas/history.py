from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from . import episode

# Shared properties
class HistoryBase(BaseModel):
    progress: Optional[int]

# Properties to receive on creation
class HistoryCreate(HistoryBase):
    progress: int

# Properties to receive on update
class HistoryUpdate(HistoryBase):
    pass

# Properties shared by models stored in DB
class HistoryInDBBase(HistoryBase):
    class Config:
        orm_mode = True

# Properties to return to client
class History(HistoryInDBBase):
    latest_read: datetime
    progress: int
    episode: episode.Episode

# Properties properties stored in DB
class HistoryInDB(HistoryInDBBase):
    id: int
    user_id: int
    episode_id: int