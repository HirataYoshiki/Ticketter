"""
 In-Out scheme about Userdata
"""

from typing import Optional
from pydantic import BaseModel

class UserIn(BaseModel):
  uid: str

class UserOut(BaseModel):
  uid: str
  ticketmax: Optional[int] = 3 
  # set 'optional' to be able to change value
  # I am planning to change value if user pay for ticket.