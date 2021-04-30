"""
Function:
1. get JWT(id_token) from frontend header 'Authorization: '
2. verify JWT with firebase_admin.auth.verify_id_token(...)
3. if true, return User
"""

from typing import Optional

from fastapi import Depends, APIRouter, HTTPException, Header

import firebase_admin
import firebase_admin.auth

async def verify_id_token(Authorization: Optional[str] = Header(None))-> dict:
  try:
    verified_user_data = firebase_admin.auth.verify_id_token(Authorization)
    return verified_user_data
  except firebase_admin.auth.InvalidIdTokenError as e:
    raise HTTPException(status_code = 400, detail = e.default_message)
  except Exception as e:
    raise HTTPException(status_code = e.code, detail = e.message)