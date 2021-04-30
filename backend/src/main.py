import os

from fastapi import FastAPI
import uvicorn

import firebase_admin
from firebase_admin import credentials

from apps.app_routers import routers

cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIAL_FILE_PATH'))
firebase_admin.initialize_app(cred)


app=FastAPI()
for router in routers:
  app.include_router(router)
"""
  
@app.on_event("startup")
async def startup():
  engine.connect()

@app.on_event("shutdown")
async def shutdown():
  engine.disconnect()
  
"""

# this is just for test------------------------------------------------------
from pydantic import BaseModel
from fastapi import Depends
import os, json
with open(os.getenv('IDPLATFORM_API_KEY_FILE_PATH'),'r') as f:
  PAYLOAD = json.load(f)
  API_KEY = PAYLOAD['API_KEY']
class IdTokenInput(BaseModel):
  email: str
  password: str

@app.post('/test/getidtoken')
async def get_id_token(inputs: IdTokenInput):
  import requests
  url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
  payload = {
    "email": inputs.email,
    "password": inputs.password,
    "returnSecureToken": True
  }
  response = requests.post(url, payload)
  id_token = json.loads(response.content)['idToken']
  return {"id_token": id_token}
#-----------------------------------------------------------------------------------------------

if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=8080)