from datetime import date

from pydantic import BaseModel


class Company(BaseModel):  #serializer
    id: int
    name: str
    link: str
    city: str
    date_added: date
    contact_first_name: str
    contact_last_name: str
    contact_phone_number: str
    contact_email: str
    company_id: int
    country: str

    class Config:
        orm_mode = True


class Vacancy(BaseModel):  #serializer
    id = int
    position_name = str
    company_id = int
    salary = float
    max_experience: int
    vacancy_id: int
    vacancy_link: str
    min_experience: int
    skills: str

    class Config:
        orm_mode = True
