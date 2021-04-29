import os

from fastapi import FastAPI
import uvicorn
import firebase_admin

from firebase_admin import credentials
from auth import router as authrouter

cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIAL_FILE_PATH'))
firebase_admin.initialize_app(cred)
#from Routers import ROUTERS
#from db import engine


#for router in ROUTERS:
#  app.include_router(router)
app=FastAPI()
app.include_router(authrouter)
"""
  
@app.on_event("startup")
async def startup():
  engine.connect()

@app.on_event("shutdown")
async def shutdown():
  engine.disconnect()
  
"""

if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=8080)