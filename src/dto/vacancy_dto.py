
from pydantic import BaseModel


class VacancyDto(BaseModel):  # serializer
    position_name: str
    company_id: int
    salary: float
    max_experience: int
    vacancy_id: int
    vacancy_link: str
    min_experience: int
    skills: str

    class Config:
        orm_mode = True
