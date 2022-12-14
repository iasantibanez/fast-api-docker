from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Departments(Base):
    id = Column(Integer,primary_key=True,index=True)
    department = Column(String,unique=True,nullable=False)