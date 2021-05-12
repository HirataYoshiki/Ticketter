from datetime import datetime
from typing import Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_

from auth import verify_id_token, UserTokendata
from apps.Interactions import Schemes
from apps.Interactions import Models
from apps.Tickets.Models import Tickets

from db import get_session

from sqlalchemy.orm.exc import NoResultFound

import firebase_admin
from firebase_admin.auth import UserNotFoundError


async def give_a_ticket(
  uid: str,
  interaction: Schemes.TicketInteractionIn, 
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)) -> Schemes.TicketInteractionOut:
  try:
    ticketmax:int = session.query(Tickets).filter(Tickets.ticketid == interaction.ticketid).one().volumemax
    ticketnow:int = session.query(Models.Interactions).filter(Models.Interactions.ticketid == interaction.ticketid).count()
    if ticketnow >= ticketmax:
      raise HTTPException(status_code = 400, detail = f"Luck of ticket. Number of ticket_max is {ticketmax}")
    firebase_admin.auth.get_user(uid)
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
  except ValueError:
    raise HTTPException(status_code=400)
  except UserNotFoundError as e:
    raise HTTPException(status_code=404, detail=e.default_message)
  except:
    raise HTTPException(status_code=400, detail="Error occured.")

async def give_tickets(
  interactions: Schemes.TicketInteractionMultiIn,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
):
  try:
    ticketmax:int = session.query(Tickets).filter(Tickets.ticketid == interactions.ticketid).one().volumemax
    ticketnow:int = session.query(Models.Interactions).filter(Models.Interactions.ticketid == interactions.ticketid).count()
    ticketfuture:int = len(interactions.to_)
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
    results = session.query(Models.Interactions).filter(
      Models.Interactions.from_ == token.user_id,
      Models.Interactions.ticketid == interactions.ticketid
    ).all()
    return list(map(lambda x: Schemes.TicketInteractionOut(**x.__dict__),results))
  except:
    raise HTTPException(status_code=400, detail="Error Occuered. try it again")

async def delete_my_given_tickets(
  ticketids: Schemes.TicketInteractionMultiDeleteIn,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)):
  try:
    deletes = Models.Interactions.__table__.delete().where(
      and_(
        Models.Interactions.__table__.c.to_ == token.user_id,
        Models.Interactions.__table__.c.ticketid.in_(ticketids.interactionidList)
      )
    )
    session.execute(deletes)
    session.commit()
    return  ticketids.interactionidList
  except:
    raise HTTPException(status_code = 400)

async def get_interactions(
  from_: Optional[str] = None,
  to_: Optional[str] = None,
  token: UserTokendata = Depends(verify_id_token),
  session: Session = Depends(get_session)
):
  try:
    if (from_ and to_):
      query = session.query(Models.Interactions).filter(or_(
        Models.Interactions.from_ == from_,
        Models.Interactions.to_ == to_
      ))
    elif from_:
      query = session.query(Models.Interactions).filter(
        Models.Interactions.from_ == from_
      )
    elif to_:
      query = session.query(Models.Interactions).filter(
        Models.Interactions.to_ == to_
      )
    else:
      query = session.query(Models.Interactions)
    return list(map(lambda x: Schemes.TicketInteractionOut(**x.__dict__), query.all()))
  except:
    raise HTTPException(status_code=400)