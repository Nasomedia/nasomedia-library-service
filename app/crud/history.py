from typing import List, Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


from app.crud.base import CRUDBase
from app.models import History
from app.schemas import HistoryCreate, HistoryUpdate

from app.utils import get_kst_now

class CRUDHistory(CRUDBase[History, HistoryCreate, HistoryUpdate]):
    def get_multi_with_user(
        self, db: Session, *, user_id: int
    ) -> List[History]:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .all()

    def get_with_user_and_episode(
        self, 
        db: Session, 
        *, 
        user_id:int, 
        episode_id: int
    ) -> List[History]:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .filter(self.model.episode_id == episode_id)\
            .first()

    def create_with_user_and_episode(
        self, db: Session,
        *,
        obj_in: HistoryCreate,
        user_id: int,
        episode_id: int
    ) -> History:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            **obj_in_data, 
            user_id=user_id, 
            episode_id=episode_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session,
        *,
        db_obj: History,
        obj_in: HistoryUpdate
    ) -> History:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        setattr(db_obj, "latest_date", get_kst_now())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
        
history = CRUDHistory(History)