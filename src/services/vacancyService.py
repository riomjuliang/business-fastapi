from fastapi import HTTPException

from src.database.dataSourceConfiguration import SessionLocal
from src.database.models.vacancy import Vacancy
from src.dto.vacancyDto import VacancyDto
from src.repository import companyRepository
from src.repository import vacancyRepository

db = SessionLocal()


class VacancyService:

    def create_vacancy(self, vacancy: VacancyDto):
        existing_company = companyRepository.get_company_by_id(vacancy.company_id)
        if not existing_company:
            raise HTTPException(status_code=404, detail="Company with id " + str(vacancy.company_id) + " not exists")

        existing_vacancy = vacancyRepository.get_vacancy_by_id(vacancy.vacancy_id)
        if existing_vacancy:
            raise HTTPException(status_code=400,
                                detail="Vacancy with id " + str(vacancy.vacancy_id) + " already exists")

        to_create_vacancy = Vacancy(
            position_name=vacancy.position_name,
            company_id=vacancy.company_id,
            salary=vacancy.salary,
            max_experience=vacancy.max_experience,
            vacancy_id=vacancy.vacancy_id,
            vacancy_link=vacancy.vacancy_link,
            min_experience=vacancy.min_experience,
            skills=vacancy.skills
        )

        db.add(to_create_vacancy)
        db.commit()
        db.refresh(to_create_vacancy)

        return to_create_vacancy

    def get_vacancies(self):
        return vacancyRepository.get_all()

    def get_vacancy_by_id(self, vacancy_id: int):
        vacancy = vacancyRepository.get_vacancy_by_id(vacancy_id)
        if vacancy is None:
            raise HTTPException(status_code=404, detail="Vacancy with vacancy id " + str(vacancy_id) + " not found")
        else:
            return vacancy

    def update_vacancy(self, vacancy_id: int, vacancy: VacancyDto):
        vacancy_to_update = vacancyRepository.get_vacancy_by_id(vacancy_id)
        if vacancy_to_update is None:
            raise HTTPException(status_code=404, detail="Vacancy with vacancy id " + str(vacancy_id) + " not found")
        else:
            vacancy_to_update.position_name = vacancy.position_name
            vacancy_to_update.company_id = vacancy.company_id,
            vacancy_to_update.salary = vacancy.salary,
            vacancy_to_update.max_experience = vacancy.max_experience,
            vacancy_to_update.vacancy_link = vacancy.vacancy_link,
            vacancy_to_update.min_experience = vacancy.min_experience,
            vacancy_to_update.skills = vacancy.skills

            db.commit()

            return vacancy_to_update

    def delete_vacancy(self, vacancy_id: int):
        vacancy_to_delete = vacancyRepository.get_vacancy_by_id(vacancy_id)
        if vacancy_to_delete is None:
            raise HTTPException(status_code=404, detail="Vacancy with vacancy id " + str(vacancy_id) + " not found")
        else:
            db.delete(vacancy_to_delete)
            db.commit()

            return vacancy_to_delete

    def get_vacancies_by_company_id(self, company_id):
        vacancies = vacancyRepository.get_all_by_company_id(company_id)

        if not vacancies:
            raise HTTPException(status_code=404, detail="Vacancies with company id " + str(company_id) + " not found")
        else:
            return vacancies
