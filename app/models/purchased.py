from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.utils import get_kst_now

from app.db import Base

class Purchased(Base):
    __tablename__ = "purchased"
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)
    episode_id = Column(Integer, nullable=False)