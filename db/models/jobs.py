from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Jobs(Base):
    id = Column(Integer,primary_key=True,index=True)
    job = Column(String,unique=True,nullable=False)