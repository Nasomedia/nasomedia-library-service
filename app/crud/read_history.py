from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import ReadHistory, read_history
from app.schemas import ReadHistoryCreate, ReadHistoryUpdate

class CRUDReadHistory(CRUDBase[ReadHistory, ReadHistoryCreate, ReadHistoryUpdate]):
    pass

read_history = CRUDReadHistory(ReadHistory)