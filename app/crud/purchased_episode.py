from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import PurchasedEpisode, purchased_episode
from app.schemas import PurchasedEpisodeCreate, PurchasedEpisodeUpdate

class CRUDPurchasedEpisode(CRUDBase[PurchasedEpisode, PurchasedEpisodeCreate, PurchasedEpisodeUpdate]):
    pass

purchased_episode = CRUDPurchasedEpisode(PurchasedEpisode)