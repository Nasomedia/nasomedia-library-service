from typing import Optional
from pydantic import BaseModel

# Shared properties
class ModelFrameBase(BaseModel):
    name: Optional[str] = None

# Properties to receive on creation
class ModelFrameCreate(ModelFrameBase):
    name: str

# Properties to receive on update
class ModelFrameUpdate(ModelFrameBase):
    pass

# Properties shared by models stored in DB
class ModelFrameInDBBase(ModelFrameBase):
    id: int
    
    name: str

    class Config:
        orm_mode = True

# Properties to return to client
class ModelFrame(ModelFrameInDBBase):
    pass

# Properties properties stored in DB
class ModelFrameInDB(ModelFrameInDBBase):
    pass