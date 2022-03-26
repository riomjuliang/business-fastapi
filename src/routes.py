from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.controllers import companyController
from src.database import schemas
from src.database.scripts import get_db

router = APIRouter()


@router.post("/companies/", response_model=schemas.Company)
def create_user(company: schemas.Company, db: Session = Depends(get_db)):
    try:
        return companyController.create_company(company, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/companies/", response_model=List[schemas.Company])
def get_companies(db: Session = Depends(get_db)):
    return companyController.get_companies(db=db)


@router.get("/companies/{company_name}", response_model=schemas.Company)
def get_company_by_name(company_name, db: Session = Depends(get_db)):
    try:
        return companyController.get_company_by_name(company_name, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/companies/{company_id}", response_model=schemas.Company)
def get_company_by_id(company_id, db: Session = Depends(get_db)):
    try:
        return companyController.get_company_by_id(company_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
