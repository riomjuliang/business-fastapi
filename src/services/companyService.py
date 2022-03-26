from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.database import schemas, models


class CompanyService:
    def create_company(self, db: Session, company: schemas.Company):
        existing_company = self.get_company_by_name(db, name=company.name)
        if existing_company:
            raise HTTPException(status_code=400, detail="Company already exists")

        to_create_company = models.Company(
            name=company.name,
            link=company.link,
            city=company.city,
            date_added=company.date_added,
            contact_first_name=company.contact_first_name,
            contact_last_name=company.contact_last_name,
            contact_phone_number=company.contact_phone_number,
            contact_email=company.contact_email,
            company_id=company.company_id,
            country=company.country
        )

        db.add(to_create_company)
        db.commit()
        db.refresh(to_create_company)
        return to_create_company

    def get_companies(self, db: Session):
        return db.query(models.Company).all()

    def get_company_by_id(self, db: Session, company_id: int):
        company = db.query(models.Company).filter(models.Company.company_id == company_id).first()
        if company is None:
            raise HTTPException(status_code=404, detail="Company with company id " + str(company_id) + " not exists")
        else:
            return company
