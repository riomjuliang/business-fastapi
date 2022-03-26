from src.services import companyService


def create_company(company, db):
    cs = companyService.CompanyService()
    return cs.create_company(db=db, company=company)


def get_companies(db):
    cs = companyService.CompanyService()
    return cs.get_companies(db=db)


def get_company_by_name(name, db):
    cs = companyService.CompanyService()
    return cs.get_company_by_name(db=db, name=name)


def get_company_by_id(company_id, db):
    cs = companyService.CompanyService()
    return cs.get_company_by_id(db=db, company_id=company_id)
