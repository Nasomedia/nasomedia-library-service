from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql.expression import null
from app.utils import get_kst_now

from app.db import Base

class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)

    latest_date = Column(DateTime(timezone=True), nullable=False, default=get_kst_now)
    progress = Column(Integer, nullable=False, default=0)

    user_id = Column(Integer, nullable=False)
    episode_id = Column(Integer, nullable=False)
