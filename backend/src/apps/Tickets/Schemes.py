from typing import Optional
from pydantic import BaseModel
from datetime import datetime
"""
#1...in api/v1, we decide that the input to 'to_' is twiiter id
     so that the ticket data is strongly connect to twitter data.
"""

class TicketIn(BaseModel):
  name: str
  to_: str #1
  text: str

class TicketOut(BaseModel):
  id: int
  name: str
  from_: str #1
  to_: str #1
  text: str
  timestamp: datetime