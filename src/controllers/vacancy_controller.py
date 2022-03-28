from src.services import vacancy_service

cs = vacancy_service.VacancyService()


def create_vacancy(vacancy):
    return cs.create_vacancy(vacancy=vacancy)


def get_vacancies():
    return cs.get_vacancies()


def get_vacancy_by_id(vacancy_id):
    return cs.get_vacancy_by_id(vacancy_id=vacancy_id)


def update_vacancy(vacancy_id, vacancy):
    return cs.update_vacancy(vacancy_id=vacancy_id, vacancy=vacancy)


def delete_vacancy(vacancy_id):
    return cs.delete_vacancy(vacancy_id=vacancy_id)


def get_all_by_company_id(company_id):
    return cs.get_vacancies_by_company_id(company_id=company_id)
