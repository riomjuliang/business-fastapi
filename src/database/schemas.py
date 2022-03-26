from pydantic import BaseModel
from pydantic.schema import datetime


class CompanyBase(BaseModel):
    companyId: int
    name: str
    link: str
    city: str
    dateAdded: datetime
    contactFirstName: str
    contactLastName: str
    contactPhoneNumber: str
    contactEmail: str
    country: str


class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True
