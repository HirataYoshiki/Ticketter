from fastapi import APIRouter, Depends
from apps.Users import Schemes
from apps.Users import Controls

router = APIRouter(prefix='/users')

@router.get('/{uid}', response_model = Schemes.UserOut)
async def get_user_by_uid(user: Schemes.UserOut = Depends(Controls.get_user_by_uid)):
  return user