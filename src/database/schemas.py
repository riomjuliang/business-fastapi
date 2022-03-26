from pydantic import BaseModel
from pydantic.schema import datetime


class Company(BaseModel):
    id: int
    name: str
    link: str
    city: str
    date_added: datetime
    contact_first_name: str
    contact_last_name: str
    contact_phone_number: str
    contact_email: str
    company_id: int
    country: str


class Vacancy(BaseModel):
    id = int
    position_name = str
    company_id = int
    salary = float
    max_experience: int
    vacancy_id: int
    vacancy_link: str
    min_experience: int
    skills: str
