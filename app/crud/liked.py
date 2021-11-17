from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Liked
from app.schemas import LikedCreate, LikedUpdate

class CRUDLiked(CRUDBase[Liked, LikedCreate, LikedUpdate]):
    pass

liked = CRUDLiked(Liked)