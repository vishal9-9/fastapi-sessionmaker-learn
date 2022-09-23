from database.engine import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func


class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, nullable=False)
    roles = Column(String, nullable=False)
    updated_at = Column(TIMESTAMP, default=func.now())
