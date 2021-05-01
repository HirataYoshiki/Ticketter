import os, json

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open(os.getenv('CLOUD_MYSQL_IDPASS_FILE_PATH'),'r') as f:
    sqlcontent = json.load(f)
    db_pass = sqlcontent['password']
    db_user = sqlcontent['username']
    db_name = sqlcontent['db_name']
    db_hostname = sqlcontent['host']
    db_port = sqlcontent['port']
    cloud_sql_connection_name = sqlcontent['cloud_sql_connection_name']


engine = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            host=db_hostname,
            database=db_name
        ),
        echo=True
    )

SessionLocal = sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
    )

def get_session():
    db = SessionLocal() # sessionを生成
    try:
        yield db
    finally:
        db.close()

Base=declarative_base()