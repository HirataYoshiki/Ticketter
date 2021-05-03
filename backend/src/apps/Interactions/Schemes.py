from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class TicketInteractionIn(BaseModel):
  ticketid: int

class TicketInteractionOut(BaseModel):
  ticketid: int
  from_: str
  to_: str
  timestamp: datetime

class TicketInteractionMultiIn(BaseModel):
  ticketid: int
  to_: List[str]

class TicketInteractionMultiOut(BaseModel):
  interactionList: List[TicketInteractionOut]

class TicketInteractionMultiDeleteIn(BaseModel):
  interactionList: List[str]