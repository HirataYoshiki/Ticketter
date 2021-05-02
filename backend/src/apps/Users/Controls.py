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
    user = session.query(Models.Users).filter(Models.Users.uid == uid).one()
    return Schemes.UserOut(**user.__dict__)
  except NoResultFound as e:
    raise HTTPException(status_code = 404, detail = "No user Found")
  except Exception as e:
    raise HTTPException(status_code = e.code if e.code else 400, detail = e.message if e.message else "error")

async def create_user(userdata: UserTokendata = Depends(verify_id_token), session:Session=Depends(get_session)):
  try:
    #user = session.query(Models.Users).filter(Models.Users.uid == userdata.user_id).first()
    #if user:
      #return Schemes.UserOut(**user)
    adds = Models.Users(uid = userdata.user_id, ticketmax = 3)
    session.add(adds)
    session.commit()
    return Schemes.UserOut(**adds.__dict__)
  except Exception as e:
    raise HTTPException(status_code = e.status_code if e.status_code else 400)
    