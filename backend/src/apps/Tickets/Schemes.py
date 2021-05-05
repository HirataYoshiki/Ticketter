from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TicketIn(BaseModel):
  name: str
  text: str
  volumemax: Optional[int] = 100

class TicketOut(BaseModel):
  ticketid: int
  uid: str
  name: str
  text: str
  timestamp: datetime
  volumemax: int