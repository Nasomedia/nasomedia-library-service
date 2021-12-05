from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Purchased
from app.schemas import PurchasedCreate, PurchasedUpdate

class CRUDPurchased(CRUDBase[Purchased, PurchasedCreate, PurchasedUpdate]):
    def get_multi_with_user(
        self, db: Session, *, user_id: int
    ) -> List[Purchased]:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .all()

    def get_with_user(
        self, db: Session, *, episode_id: int, user_id: int
    ) -> Purchased:
        return db.query(self.model)\
            .filter(self.model.episode_id == episode_id)\
            .filter(self.model.user_id == user_id)\
            .all()

    def get_with_user_and_episode(
        self, 
        db: Session, 
        *, 
        user_id:int, 
        episode_id: int
    ) -> Purchased:
        return db.query(self.model)\
            .filter(self.model.user_id == user_id)\
            .filter(self.model.episode_id == episode_id)\
            .first()

    def create_with_user_episode(
        self, db: Session, *, user_id: int, episode_id: int
    ) -> Purchased:
        db_obj = self.model(
            user_id=user_id, 
            episode_id=episode_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

purchased = CRUDPurchased(Purchased)