from sqlalchemy import Column, Integer, String, Float

from src.database import Base


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, autoincrement=True)
    position_name = Column(String(255), nullable=False)
    company_id = Column(Integer)
    salary = Column(Float)
    max_experience = Column(Integer)
    vacancy_id = Column(Integer, primary_key=True)
    vacancy_link = Column(String(255))
    min_experience = Column(Integer)
    skills = Column(String(255))