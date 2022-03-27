from datetime import date

from pydantic import BaseModel


class CompanyDto(BaseModel):  # serializer
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
