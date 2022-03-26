from sqlalchemy import Integer, Column, String, Date, Float

from src.database.database import Base


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    link = Column(String(255))
    city = Column(String(255))
    date_added = Column(Date)
    contact_first_name = Column(String(255))
    contact_last_name = Column(String(255))
    contact_phone_number = Column(String(255))
    contact_email = Column(String(255))
    company_id = Column(Integer, nullable=False)
    country = Column(String(255))


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    position_name = Column(String(255), nullable=False)
    company_id = Column(Integer)
    salary = Column(Float)
    max_experience = Column(Integer)
    vacancy_id = Column(Integer)
    vacancy_link = Column(String(255))
    min_experience = Column(Integer)
    skills = Column(String(255))
