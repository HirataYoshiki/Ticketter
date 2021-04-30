from fastapi import Depends, HTTPException

from auth import verify_id_token
from apps.Users import Schemes

import firebase_admin
import firebase_admin.auth
import firebase_admin.exceptions

async def get_user_by_uid(uid: str, userdata:dict = Depends(verify_id_token)):
  try:
    userdata = firebase_admin.auth.get_user(uid)
    return Schemes.UserOut(uid = uid)
  except firebase_admin.auth.UserNotFoundError as e:
    raise HTTPException(status_code = 400, detail = e.default_message)
  except Exception as e:
    raise HTTPException(status_code = e.code, detail = e.message)