from datetime import datetime
from typing import Optional
from operator import and_

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.elements import or_

from auth import verify_id_token, UserTokendata
from apps.Interactions import Schemes
from apps.Interactions import Models
from apps.Tickets.Models import Tickets

from db import get_session

from sqlalchemy.orm.exc import NoResultFound

async def give_a_ticket(
  uid: str,
  interaction: Schemes.TicketInteractionIn, 
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)) -> Schemes.TicketInteractionOut:
  ticketmax:int = session.query(Tickets).filter(Tickets.ticketid == interaction.ticketid).volumemax
  ticketnow:int = session.query(Models.Interactions).filter(Models.Interactions.ticketid == interaction.ticketid).count()
  if ticketnow >= ticketmax:
    raise HTTPException(status_code = 400, detail = f"Luck of ticket. Number of ticket_max is {ticketmax}")
  adds = Models.Interactions(
    **interaction.dict(),
    to_ = uid,
    from_ = token.user_id,
    timestamp = datetime.now()
  )
  session.add(adds)
  session.commit()
  session.refresh(adds)
  return Schemes.TicketInteractionOut(
    **session.query(Models.Interactions).filter(
      Models.Interactions.ticketid == interaction.ticketid,
      Models.Interactions.from_ == token.user_id).one().__dict__
  )

async def give_tickets(
  interactions: Schemes.TicketInteractionMultiIn,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
):
  ticketmax:int = session.query(Tickets).filter(Tickets.ticketid == interactions.ticketid).volumemax
  ticketnow:int = session.query(Models.Interactions).filter(Models.Interactions.ticketid == interactions.ticketid).count()
  ticketfuture:int = len(interactions)
  if (ticketnow >= ticketmax or (ticketnow + ticketfuture) > ticketmax):
    raise HTTPException(status_code = 400, detail=f"Luck of ticket. Number of ticket_max is {ticketmax}")
  timestamp = datetime.now()
  interactionadds = [{
    "ticketid": interactions.ticketid,
    "to_": to_,
    "from_": token.user_id,
    "timestamp": timestamp} for to_ in interactions.to_]
  session.execute(Models.Interactions.__table__.insert(), interactionadds)
  session.commit()

async def delete_my_given_ticket(
  ticketid: int,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)):
  try:
    target = session.query(Models.Interactions).filter(
      Models.Interactions.to_ == token.user_id,
      Models.Interactions.ticketid == ticketid
    ).one_or_none()
    if not target:
      raise HTTPException(status_code = 400, detail = f"No ticket found. ticketid: {ticketid}")
    session.delete(target)
    session.commit()
    return {"delete": ticketid}
  except:
    raise HTTPException(status_code = 400)

async def delete_my_given_tickets(
  ticketids: Schemes.TicketInteractionMultiDeleteIn,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)):
  try:
    deletes = Models.Interactions.__table__.delete().where(
      and_(
        Models.Interactions.__table__.c.to_ == token.user_id,
        Models.Interactions.__table__.c.ticketid.in_(ticketids)
      )
    )
    session.execute(deletes)
    session.commit()
    return {
      "delete": ticketids
    }
  except:
    raise HTTPException(status_code = 400)

async def get_interactions(
  uid: str,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
):
  try:
    gets = Models.Interactions.__table__.select().where(or_(
      Models.Interactions.__table__.c.from_ == uid,
      Models.Interactions.__table__.c.to_ == uid
    ))
    selects = session.execute(gets)
    return selects