from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.controllers import companyController
from src.database import schemas
from src.database.scripts import get_db

router = APIRouter()


@router.post("/companies", response_model=schemas.Company, status_code=status.HTTP_201_CREATED)
def create_company(company: schemas.Company, db: Session = Depends(get_db)):
    return companyController.create_company(company, db=db)


@router.get("/companies", response_model=List[schemas.Company])
def get_companies(db: Session = Depends(get_db)):
    return companyController.get_companies(db=db)


@router.get("/companies/{company_id}", response_model=schemas.Company)
def get_company_by_id(company_id, db: Session = Depends(get_db)):
    return companyController.get_company_by_id(company_id, db=db)
