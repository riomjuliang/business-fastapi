from typing import List

from fastapi import APIRouter, status

from src.controllers import company_controller, vacancy_controller
from src.dto.company_dto import CompanyDto
from src.dto.vacancy_dto import VacancyDto

router = APIRouter()

# Companies

@router.post("/companies", response_model=CompanyDto, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyDto):
    return company_controller.create_company(company)


@router.get("/companies", response_model=List[CompanyDto])
def get_companies():
    return company_controller.get_companies()


@router.get("/companies/{company_id}", response_model=CompanyDto)
def get_company_by_id(company_id: int):
    return company_controller.get_company_by_id(company_id)


@router.put("/companies/{company_id}", response_model=CompanyDto)
def update_company(company_id: int, company: CompanyDto):
    return company_controller.update_company(company_id, company)


@router.delete("/companies/{company_id}", response_model=CompanyDto)
def delete_company(company_id: int):
    return company_controller.delete_company(company_id)


# Vacancies

@router.post("/vacancies", response_model=VacancyDto, status_code=status.HTTP_201_CREATED)
def create_vacancy(vacancy: VacancyDto):
    return vacancy_controller.create_vacancy(vacancy)


@router.get("/vacancies", response_model=List[VacancyDto])
def get_vacancies():
    return vacancy_controller.get_vacancies()


@router.get("/vacancies/{vacancy_id}", response_model=VacancyDto)
def get_vacancy_by_id(vacancy_id: int):
    return vacancy_controller.get_vacancy_by_id(vacancy_id)


@router.put("/vacancies/{vacancy_id}", response_model=VacancyDto)
def update_vacancy(vacancy_id: int, vacancy: VacancyDto):
    return vacancy_controller.update_vacancy(vacancy_id, vacancy)


@router.delete("/vacancies/{vacancy_id}", response_model=VacancyDto)
def delete_vacancy(vacancy_id: int):
    return vacancy_controller.delete_vacancy(vacancy_id)


@router.get("/vacancies/company/{company_id}", response_model=List[VacancyDto])
def get_vacancies_by_company_id(company_id: int):
    return vacancy_controller.get_all_by_company_id(company_id)
