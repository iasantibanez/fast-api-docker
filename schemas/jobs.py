from typing import Optional
from pydantic import BaseModel


#properties required during job creation
class JobsCreate(BaseModel):
    id: int
    job : str