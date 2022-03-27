from src.services import companyService

cs = companyService.CompanyService()


def create_company(company):
    return cs.create_company(company=company)


def get_companies():
    return cs.get_companies()


def get_company_by_id(company_id):
    return cs.get_company_by_id(company_id=company_id)


def update_company(company_id, company):
    return cs.update_company(company_id=company_id, company=company)


def delete_company(company_id):
    return cs.delete_company(company_id=company_id)
