from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import History
from app.schemas import HistoryCreate, HistoryUpdate

class CRUDHistory(CRUDBase[History, HistoryCreate, HistoryUpdate]):
    pass

history = CRUDHistory(History)