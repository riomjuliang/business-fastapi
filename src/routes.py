from typing import List

from fastapi import APIRouter, status

from src.controllers import companyController, vacancyController
from src.dto.companyDto import CompanyDto
from src.dto.vacancyDto import VacancyDto

router = APIRouter()

# Companies

@router.post("/companies", response_model=CompanyDto, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyDto):
    return companyController.create_company(company)


@router.get("/companies", response_model=List[CompanyDto])
def get_companies():
    return companyController.get_companies()


@router.get("/companies/{company_id}", response_model=CompanyDto)
def get_company_by_id(company_id: int):
    return companyController.get_company_by_id(company_id)


@router.put("/companies/{company_id}", response_model=CompanyDto)
def update_company(company_id: int, company: CompanyDto):
    return companyController.update_company(company_id, company)


@router.delete("/companies/{company_id}", response_model=CompanyDto)
def delete_company(company_id: int):
    return companyController.delete_company(company_id)


# Vacancies

@router.post("/vacancies", response_model=VacancyDto, status_code=status.HTTP_201_CREATED)
def create_vacancy(vacancy: VacancyDto):
    return vacancyController.create_vacancy(vacancy)


@router.get("/vacancies", response_model=List[VacancyDto])
def get_vacancies():
    return vacancyController.get_vacancies()


@router.get("/vacancies/{vacancy_id}", response_model=VacancyDto)
def get_vacancy_by_id(vacancy_id: int):
    return vacancyController.get_vacancy_by_id(vacancy_id)


@router.put("/vacancies/{vacancy_id}", response_model=VacancyDto)
def update_vacancy(vacancy_id: int, vacancy: VacancyDto):
    return vacancyController.update_vacancy(vacancy_id, vacancy)


@router.delete("/vacancies/{vacancy_id}", response_model=VacancyDto)
def delete_vacancy(vacancy_id: int):
    return vacancyController.delete_vacancy(vacancy_id)


@router.get("/vacancies/company/{company_id}", response_model=List[VacancyDto])
def get_vacancies_by_company_id(company_id: int):
    return vacancyController.get_all_by_company_id(company_id)
