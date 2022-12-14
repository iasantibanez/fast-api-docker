from typing import Optional
from pydantic import BaseModel


#properties required during employee creation
class EmployeesCreate(BaseModel):
    id: int
    name : str
    datetime : str
    department_id : Optional[int]
    job_id : Optional[int]