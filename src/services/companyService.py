from sqlalchemy.orm import Session

from src.database import schemas, models


class CompanyService:
    def create_company(self, db: Session, company: schemas.Company):
        existing_company = self.get_company_by_name(db, name=company.name)
        if existing_company:
            raise Exception("Company already exists")

        to_create_company = models.Company(
            name=company.name,
            link=company.link,
            city=company.city,
            dateAdded=company.date_added,
            contactFirstName=company.contact_first_name,
            contactLastName=company.contact_last_name,
            contactPhoneNumber=company.contact_phone_number,
            contactEmail=company.contact_email,
            companyId=company.company_id,
            country=company.country
        )

        db.add(to_create_company)
        db.commit()
        db.refresh(to_create_company)
        return to_create_company

    def get_companies(self, db: Session):
        return db.query(models.Company).all()

    def get_company_by_name(self, db: Session, name: str):
        return db.query(models.Company).filter(models.Company.name == name).first()

    def get_company_by_id(self, db: Session, company_id: int):
        return db.query(models.Company).filter(models.Company.companyId == company_id).first()
