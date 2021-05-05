import os

from fastapi import FastAPI
import uvicorn

import firebase_admin
from firebase_admin import credentials

from db import engine, Base
from apps.app_routers import routers

cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIAL_FILE_PATH'))
firebase_admin.initialize_app(cred)


app=FastAPI()
for router in routers:
  app.include_router(router)

  
@app.on_event("startup")
async def startup():
  engine.connect()

Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def shutdown():
  engine.disconnect()


if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=8080)