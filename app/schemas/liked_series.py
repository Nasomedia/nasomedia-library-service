from typing import Optional, List
from pydantic import BaseModel
from . import series

# Shared properties
class LikedSeriesBase(BaseModel):
    series_id: Optional[int]

# Properties to receive on creation
class LikedSeriesCreate(LikedSeriesBase):
    series_id: int

# Properties to receive on update
class LikedSeriesUpdate(LikedSeriesBase):
    pass

# Properties shared by models stored in DB
class LikedSeriesInDBBase(LikedSeriesBase):
    class Config:
        orm_mode = True

# Properties to return to client
class LikedSeries(LikedSeriesInDBBase):
    series: series.Series

# Properties properties stored in DB
class LikedSeriesInDB(LikedSeriesInDBBase):
    id: int
    user_id: int
    series_id: int