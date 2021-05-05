from typing import List

from fastapi import APIRouter, Depends
from apps.Users import Schemes
from apps.Users import Controls

router = APIRouter()
@router.post('/users', response_model = Schemes.UserOut)
async def create_user(user: Schemes.UserOut = Depends(Controls.create_user)):
  return user

@router.get('/users', response_model = List[Schemes.UserOut])
async def get_users(users: list = Depends(Controls.get_users)):
  return users

@router.get('/users/{uid}', response_model = Schemes.UserOut)
async def get_user_by_uid(user: Schemes.UserOut = Depends(Controls.get_user_by_uid)):
  return user