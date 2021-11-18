from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Liked
from app.schemas import LikedCreate, LikedUpdate

class CRUDLiked(CRUDBase[Liked, LikedCreate, LikedUpdate]):
    def get_multi_with_user(
        self, db: Session, *, user_id: int
    ) -> List[Liked]:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .all()

    def get_with_user_and_series(
        self, 
        db: Session, 
        *, 
        user_id:int, 
        series_id: int
    ) -> Liked:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .filter(self.model.series_id == series_id)\
            .first()

    def get_with_user_and_episode(
        self, 
        db: Session, 
        *, 
        user_id:int, 
        series_id: int
    ) -> Liked:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .filter(self.model.series_id == series_id)\
            .first()

    def create_with_user_and_series(
        self, db: Session,
        *,
        user_id: int,
        series_id: int
    ) -> Liked:
        db_obj = self.model(
            user_id=user_id, 
            series_id=series_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

liked = CRUDLiked(Liked)