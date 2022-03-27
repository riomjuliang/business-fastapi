from src.database.dataSourceConfiguration import SessionLocal
from src.database.models.vacancy import Vacancy

db = SessionLocal()


def get_all():
    return db.query(Vacancy).all()


def get_vacancy_by_id(vacancy_id: int):
    return db.query(Vacancy).filter(Vacancy.vacancy_id == vacancy_id).first()
