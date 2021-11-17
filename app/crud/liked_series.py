from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import LikedSeries
from app.schemas import LikedSeriesCreate, LikedSeriesUpdate

class CRUDLikedSeries(CRUDBase[LikedSeries, LikedSeriesCreate, LikedSeriesUpdate]):
    pass

liked_series = CRUDLikedSeries(LikedSeries)