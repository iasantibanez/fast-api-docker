from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Employees(Base):
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,nullable=False)
    datetime = Column(String,nullable=False)
    department_id = Column(Integer,ForeignKey("departments.id"))
    job_id = Column(Integer,ForeignKey("jobs.id"))
