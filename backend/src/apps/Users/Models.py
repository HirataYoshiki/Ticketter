from db import Base,engine

from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship


class Users(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index = True, autoincrement=True)
  uid = Column(String(255), unique=True)
  ticketmax = Column(Integer)