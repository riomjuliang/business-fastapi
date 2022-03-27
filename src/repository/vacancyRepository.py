from src.database.dataSourceConfiguration import SessionLocal
from src.database.models.vacancy import Vacancy

db = SessionLocal()


def get_all():
    return db.query(Vacancy).all()


def get_vacancy_by_id(vacancy_id: int):
    return db.query(Vacancy).filter(Vacancy.vacancy_id == vacancy_id).first()


def get_all_by_company_id(company_id: int):
    return db.query(Vacancy).filter(Vacancy.company_id == company_id).all()


def delete(vacancy: Vacancy):
    db.delete(vacancy)
    db.commit()

    return vacancy
