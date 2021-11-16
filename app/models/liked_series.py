from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.utils import get_kst_now

from app.db import Base

class LikedSeries(Base):
    __tablename__ = "liked_series"
    id = Column(Integer, primary_key=True, index=True) # series의 id

    user_id = Column(Integer, nullable=False)
