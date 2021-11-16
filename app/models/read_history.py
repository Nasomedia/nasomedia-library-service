from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.utils import get_kst_now

from app.db import Base

class ReadHistory(Base):
    __tablename__ = "read_history"
    id = Column(Integer, primary_key=True, index=True) # episode의 id

    latest_read = Column(DateTime(timezone=True), nullable=False, default=get_kst_now)
    progress = Column(Integer, nullable=False, default=0)

    user_id = Column(Integer, nullable=False)
