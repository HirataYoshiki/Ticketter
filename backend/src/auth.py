from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, HTTPException
import firebase_admin
import firebase_admin.auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()
@router.post('/token')
async def create_access_token(uid: str):
  try:
    user = firebase_admin.auth.get_user(uid)
    if user:
      return firebase_admin.auth.create_custom_token(uid)
  except Exception as e:
    raise HTTPException(status_code=400)

async def get_current_user(token: str = Depends(oauth2_scheme)):
  try:
    userdata = firebase_admin.auth.verify_id_token(token)
    return userdata
  except:
    raise HTTPException(status_code=400)

async def get_active_current_user(user = Depends(get_current_user)):
  if user['activate']:
    return user
  else:
    raise HTTPException(status_code=401)