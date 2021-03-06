from fastapi import HTTPException

from src.database import SessionLocal
from src.database.models.company import Company
from src.dto.company_dto import CompanyDto
from src.repository import company_repository

db = SessionLocal()


class CompanyService:

    def create_company(self, company: CompanyDto):
        existing_company = company_repository.get_company_by_id(company.company_id)
        if existing_company:
            raise HTTPException(status_code=400, detail="Company already exists with id " + str(company.company_id))

        existing_company_by_name = company_repository.get_company_by_name(company.name)
        if existing_company_by_name:
            raise HTTPException(status_code=400, detail="Company already exists with name " + company.name)

        to_create_company = Company(
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

    def get_companies(self):
        return company_repository.get_all()

    def get_company_by_id(self, company_id: int):
        company = company_repository.get_company_by_id(company_id)
        if company is None:
            raise HTTPException(status_code=404, detail="Company with company id " + str(company_id) + " not found")
        else:
            return company

    def update_company(self, company_id: int, company: CompanyDto):
        company_to_update = company_repository.get_company_by_id(company_id)
        if company_to_update is None:
            raise HTTPException(status_code=404, detail="Company with company id " + str(company_id) + " not found")
        else:
            company_to_update.name = company.name
            company_to_update.link = company.link
            company_to_update.city = company.city
            company_to_update.date_added = company.date_added
            company_to_update.contact_first_name = company.contact_first_name
            company_to_update.contact_last_name = company.contact_last_name
            company_to_update.contact_phone_number = company.contact_phone_number
            company_to_update.contact_email = company.contact_email
            company_to_update.country = company.country

            db.commit()

            return company_to_update

    def delete_company(self, company_id: int):
        company_to_delete = company_repository.get_company_by_id(company_id)
        if company_to_delete is None:
            raise HTTPException(status_code=404, detail="Company with company id " + str(company_id) + " not found")
        else:
            return company_repository.delete(company_to_delete)
