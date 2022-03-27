from typing import List

from fastapi import APIRouter, status

from src.controllers import companyController
from src.database import schemas

router = APIRouter()


@router.post("/companies", response_model=schemas.Company, status_code=status.HTTP_201_CREATED)
def create_company(company: schemas.Company):
    return companyController.create_company(company)


@router.get("/companies", response_model=List[schemas.Company])
def get_companies():
    return companyController.get_companies()


@router.get("/companies/{company_id}", response_model=schemas.Company)
def get_company_by_id(company_id: int):
    return companyController.get_company_by_id(company_id)


@router.put("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.Company):
    return companyController.update_company(company_id, company)


@router.delete("/companies/{company_id}", response_model=schemas.Company)
def delete_company(company_id: int):
    return companyController.delete_company(company_id)
