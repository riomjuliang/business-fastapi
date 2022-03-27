from src.database import models
from src.database.database import SessionLocal

db = SessionLocal()


def get_all():
    return db.query(models.Company).all()


def get_company_by_id(company_id: int):
    return db.query(models.Company).filter(models.Company.company_id == company_id).first()
