from database.engine import Base
from sqlalchemy import Column, Integer, String


class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, nullable=False)
    roles = Column(String, nullable=False)
