from sqlalchemy import Integer, Column, String, Date

from src.database.dataSourceConfiguration import Base


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
