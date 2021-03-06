from sqlalchemy import (
    Column,
    Integer,
    String
)

from .meta import Base

class Icon(Base):
    __tablename__ = 'icon'

    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, nullable=False)