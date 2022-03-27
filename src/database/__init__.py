import os
import re

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USER", "vrgwlbtcblpeti")
DB_PASSWORD = os.getenv("DB_PASSWORD", "bacb7426ef9987b308a22e685cc9f963fbc4c5f223ea95eede289c2708a89755")
POSTGRES_URL = os.getenv("POSTGRES_URL", "ec2-52-3-60-53.compute-1.amazonaws.com:5432/d6p1npmqrb6veh")
DATABASE_URI = "postgres://vrgwlbtcblpeti:bacb7426ef9987b308a22e685cc9f963fbc4c5f223ea95eede289c2708a89755@ec2-52-3" \
               "-60-53.compute-1.amazonaws.com:5432/d6p1npmqrb6veh "

if DATABASE_URI and DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
