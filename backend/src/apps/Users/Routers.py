from fastapi import APIRouter, Depends
from apps.Users import Schemes
from apps.Users import Controls

router = APIRouter(prefix='/users')
@router.post('/', response_model = Schemes.UserOut)
async def create_user(user: Schemes.UserOut = Depends(Controls.create_user)):
  return user

@router.get('/{uid}', response_model = Schemes.UserOut)
async def get_user_by_uid(user: Schemes.UserOut = Depends(Controls.get_user_by_uid)):
  return user