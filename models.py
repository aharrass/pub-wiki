
from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String(10), index=True, unique=True)
    long_url = Column(String(2000), index=True, unique=True)

    created_at = Column(DateTime, default=lambda : datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)
