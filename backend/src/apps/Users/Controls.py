from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from auth import verify_id_token, UserTokendata
from apps.Users import Schemes
from apps.Users import Models
from db import get_session

from sqlalchemy.orm.exc import NoResultFound

import firebase_admin
import firebase_admin.auth
import firebase_admin.exceptions

async def get_user_by_uid(uid: str, userdata: UserTokendata = Depends(verify_id_token), session: Session = Depends(get_session)):
  try:
    user = session.query(Models.Users).filter(Models.Users).one()
    return Schemes.UserOut(**user.__dict__)
  except firebase_admin.auth.UserNotFoundError as e:
    raise HTTPException(status_code = 400, detail = e.default_message)
  except Exception as e:
    raise HTTPException(status_code = e.code, detail = e.message)

async def create_user(userdata: UserTokendata = Depends(verify_id_token), session:Session=Depends(get_session)):
  try:
    user = session.query(Models.Users).filter(Models.Users.uid == userdata.localId).one()
    if user:
      return Schemes.UserOut(**user)
  except NoResultFound:
    adds = Models.Users(uid = userdata.localId, ticketmax = 3)
    session.add(adds)
    session.commit()
    session.refresh(adds)
    return Schemes.UserOut(**adds)
  except Exception as e:
    raise HTTPException(status_code = 400)
    