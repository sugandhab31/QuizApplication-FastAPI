from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database="spendsense",
user="flask-user",
password="postgres",
host="127.0.0.1",
port=5432,

URL_DATABASE = 'postgres://{0}:{1}@{2}:{3}/{4}'.format(
    user,password,host,port,database
)

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush = False, autocommit = False, bind = engine)

Base = declarative_base()