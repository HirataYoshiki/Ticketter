"""
Function:
1. get JWT(id_token) from frontend header 'Authorization: '
2. verify JWT with firebase_admin.auth.verify_id_token(...)
3. if true, return User
"""

from typing import Optional

from fastapi import Depends, APIRouter, HTTPException, Header
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

import firebase_admin
import firebase_admin.auth

api_key = APIKeyHeader(name="Authorization", auto_error=False)

class UserTokendata(BaseModel):
  user_id: str
  email: str

async def verify_id_token(authorization: str = Depends(api_key))-> UserTokendata:
  credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate token",
    headers={"WWW-Authenticate": authorization},
    )
  if authorization:
    auth = authorization.split(" ")
  if len(auth) != 2:
    raise credentials_exception
  if auth[0] != "Bearer":
    raise credentials_exception
  id_token = auth[1]
  verified_user_data = firebase_admin.auth.verify_id_token(id_token)
  return UserTokendata(**verified_user_data)