from datetime import datetime
from typing import Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from auth import verify_id_token, UserTokendata
from apps.Tickets import Schemes
from apps.Tickets import Models
from apps.Users.Models import Users
from db import get_session

from sqlalchemy.orm.exc import NoResultFound

import firebase_admin
import firebase_admin.auth
import firebase_admin.exceptions

def maxTickets(uid: str, session:Session) -> int:
  userData = session.query(Users).filter(Users.uid == uid).one_or_none()
  if userData:
    return userData.ticketmax
  raise HTTPException(status_code= 400, detail = "No user found. try again.")

def nowTickets(uid: str, session:Session) -> int:
  tickets = session.query(Models.Tickets).filter(Models.Tickets.uid == uid).count()
  return tickets

async def create_ticket(
  ticketin: Schemes.TicketIn,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
  ) -> Schemes.TicketOut:
  if maxTickets(token.user_id, session) <= nowTickets(token.user_id, session):
    raise HTTPException(status_code= 422)
  if ticketin.volumemax > 100:
    raise HTTPException(status_code=400, detail="the volume of tickets be under 100.")
  timestamp = datetime.now()
  adds = Models.Tickets(
    **ticketin.dict(),
    uid = token.user_id,
    timestamp = timestamp
  )
  session.add(adds)
  session.commit()
  session.refresh(adds)
  return Schemes.TicketOut(
    **session.query(Models.Tickets).filter(
      Models.Tickets.uid == token.user_id,
      Models.Tickets.name == ticketin.name
      ).one().__dict__
  )

async def volume_of_all_tickets(
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)) -> int:
  tickets_volume = session.query(Models.Tickets).count()
  return tickets_volume
  
async def get_tickets(
  skip: Optional[int] = 0,
  limit: Optional[int] = 100,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
):
  volume = session.query(Models.Tickets).count()
  exception = HTTPException(status_code=400, detail = f"over limit. volume: {volume}")
  if skip > volume:
    raise exception
  query = session.query(Models.Tickets)
  query = query.limit(limit)
  query = query.offset(skip)
  return list(map(lambda x: Schemes.TicketOut(**x.__dict__), query.all()))
  
async def get_ticket(
  ticketid: int,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
):
  ticket = session.query(Models.Tickets).filter(Models.Tickets.ticketid == ticketid).one()
  return Schemes.TicketOut(**ticket.__dict__)