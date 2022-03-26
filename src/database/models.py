from sqlalchemy import Integer, Column, String, Date, Float

from src.database.database import Base


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name: Column(String(255), unique=True)
    link: Column(String(255))
    city: Column(String(255))
    dateAdded: Column(Date)
    contactFirstName: Column(String(255))
    contactLastName: Column(String(255))
    contactPhoneNumber: Column(String(255))
    contactEmail: Column(String(255))
    companyId: Column(Integer)
    country: Column(String(255))


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    positionName = Column(String(255), nullable=False)
    companyId = Column(Integer)
    salary = Column(Float)
    maxExperience: Column(Integer)
    vacancyId: Column(Integer)
    vacancyLink: Column(String(255))
    minExperience: Column(Integer)
    skills: Column(String(255))
