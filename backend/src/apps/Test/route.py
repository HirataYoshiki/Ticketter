from fastapi import APIRouter,Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey

from db import Base, get_session, engine

router = APIRouter()

class Item(BaseModel):
  name: str
  content: str


class Items(Base):
  __tablename__ = "items"
  id = Column(Integer, primary_key=True)
  name = Column(String(100))
  content = Column(String(255))

@router.post('/test')
def create_item(item:Item, session = Depends(get_session)):
  adds = Items(**item.__dict__)
  session.add(adds)
  session.commit()
  return {"result": True}

@router.get('/test')
async def get_item(session = Depends(get_session)):
  item = session.query(Items).filter(Items.id == 1).one()
  return item

if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)