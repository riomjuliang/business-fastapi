import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ['DATABASE_URL']

DATABASE_URI = "postgres://vrgwlbtcblpeti:bacb7426ef9987b308a22e685cc9f963fbc4c5f223ea95eede289c2708a89755@ec2-52-3" \
               "-60-53.compute-1.amazonaws.com:5432/d6p1npmqrb6veh "

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
