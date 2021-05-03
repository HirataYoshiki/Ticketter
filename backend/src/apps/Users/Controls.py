from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from auth import verify_id_token, UserTokendata
from apps.Users import Schemes
from apps.Users import Models
from db import get_session

from sqlalchemy.orm.exc import NoResultFound

import firebase_admin
import firebase_admin.auth
import firebase_admin.exceptions

async def create_user(userdata: UserTokendata = Depends(verify_id_token), session:Session=Depends(get_session)):
  try:
    adds = Models.Users(uid = userdata.user_id, ticketmax = 3)
    session.add(adds)
    session.commit()
    return Schemes.UserOut(uid = userdata.user_id, ticketmax = 3)
  except IntegrityError:
    raise HTTPException(status_code=422, detail="the user has already registered")
  except Exception as e:
    raise HTTPException(status_code = 400)

async def get_user_by_uid(uid: str, userdata: UserTokendata = Depends(verify_id_token), session: Session = Depends(get_session)):
  try:
    user = session.query(Models.Users).filter(Models.Users.uid == uid).one()
    return Schemes.UserOut(**user.__dict__)
  except NoResultFound as e:
    raise HTTPException(status_code = 404, detail = "No user Found")
  except Exception:
    raise HTTPException(status_code = 400, detail = "error")

async def get_users(userdata: UserTokendata = Depends(verify_id_token), session: Session = Depends(get_session)):
  try:
    return session.query(Models.Users).all()
  except Exception:
    raise HTTPException(status_code=400)