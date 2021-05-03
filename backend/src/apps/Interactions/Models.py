from db import Base,engine

from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship


class Interactions(Base):
  id = Column(Integer, primary_key = True, autoincrement = True)
  ticketid = Column(Integer)
  from_ = Column(String(100))
  to_ = Column(String(100))
  timestamp = Column(DateTime)