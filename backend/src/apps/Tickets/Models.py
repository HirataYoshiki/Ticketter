from db import Base,engine

from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship


class Tickets(Base):
  __tablename__ = "tickets"
  ticketid = Column(Integer, primary_key = True, autoincrement = True)
  uid = Column(String(100))
  name = Column(String(255))
  text = Column(String(255))
  timestamp = Column(DateTime)
  volumemax = Column(Integer)