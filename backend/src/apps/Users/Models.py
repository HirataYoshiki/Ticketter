from db import Base,engine

from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship


class Users(Base):
  __tablename__ = "users"
  uid = Column(Integer, primary_key=True, index=True)
  ticketmax = Column(Integer)