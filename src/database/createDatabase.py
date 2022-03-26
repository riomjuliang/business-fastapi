from database import Base, engine
from models import Company, Vacancy

Base.metadata.create_all(engine)