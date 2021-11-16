from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import ModelFrame
from app.schemas import CreateFrame, UpdateFrame

class CRUDFrame(CRUDBase[ModelFrame, CreateFrame, UpdateFrame]):
    pass

crud_frame = CRUDFrame(ModelFrame)