from src.database import SessionLocal
from src.database.models.company import Company

db = SessionLocal()


def get_all():
    return db.query(Company).all()


def get_company_by_id(company_id: int):
    return db.query(Company).filter(Company.company_id == company_id).first()


def get_company_by_name(company_name: str):
    return db.query(Company).filter(Company.name == company_name).first()


def delete(company: Company):
    db.delete(company)
    db.commit()

    return company
