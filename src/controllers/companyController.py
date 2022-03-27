from src.services import companyService

def create_company(company):
    cs = companyService.CompanyService()
    return cs.create_company(company=company)


def get_companies():
    cs = companyService.CompanyService()
    return cs.get_companies()


def get_company_by_id(company_id):
    cs = companyService.CompanyService()
    return cs.get_company_by_id(company_id=company_id)


def update_company(company_id, company):
    cs = companyService.CompanyService()
    return cs.update_company(company_id=company_id, company=company)


def delete_company(company_id):
    cs = companyService.CompanyService()
    return cs.delete_company(company_id=company_id)
