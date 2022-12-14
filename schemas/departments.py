from typing import Optional
from pydantic import BaseModel
from db.models.departments import Departments

#properties required during deparment creation
class DepartmentsCreate(BaseModel):
    id: int
    department : str


class ShowDeparment(BaseModel):
     #id: int
     department: str
     
     class Config():
        orm_mode = True

# class Config():
#     orm_mode = True 