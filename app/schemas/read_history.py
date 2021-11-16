from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from . import episode

# Shared properties
class ReadHistoryBase(BaseModel):
    progress: Optional[int]

# Properties to receive on creation
class ReadHistoryCreate(ReadHistoryBase):
    progress: int

# Properties to receive on update
class ReadHistoryUpdate(ReadHistoryBase):
    pass

# Properties shared by models stored in DB
class ReadHistoryInDBBase(ReadHistoryBase):
    class Config:
        orm_mode = True

# Properties to return to client
class ReadHistory(ReadHistoryInDBBase):
    latest_read: datetime
    progress: int
    episode: episode.Episode

# Properties properties stored in DB
class ReadHistoryInDB(ReadHistoryInDBBase):
    id: int
    user_id: int
    episode_id: int