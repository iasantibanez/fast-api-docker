from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from schemas.departments import DepartmentsCreate,ShowDeparment
#from db.models.departments import Departments
from db.session import get_db
from db.repository.departments import create_new_derpartment,read_department_by_id,read_departments_table,departments_table_backup,truncate_departments_table,departments_table_restore_backup
from typing import List 
from utils.init_data import init_departments_table

router = APIRouter()

@router.post('/') 
def create_deparment(request : DepartmentsCreate, db: Session = Depends(get_db)):
    department = create_new_derpartment(input_department=request, db=db)
    #TO DO :mensaje de creacion sacarlo de la funcion crear y dejarlo acá para mandar response de que se crearon mas de 1 elemento
    return department

@router.post('/multiple')
def create_multiple_deparments(request : List[DepartmentsCreate], db: Session = Depends(get_db)):
    if len(request) > 1000:
        raise HTTPException(status_code=409, detail="Exceed multiple's Deparments inserts simultaneusly")
    for department in request:
        new_department = create_new_derpartment(input_department=department, db=db)
    return new_department

@router.get('/get/{id}', response_model=ShowDeparment)
def get_department_by_id(id:int, db: Session = Depends(get_db)):
    department = read_department_by_id(id,db=db)
    if not department:
        raise HTTPException(status_code=404,detail=f"deparment with this id {id} does not exist")
    return department

@router.get('/get_all/')
def get_all_departments(db: Session = Depends(get_db)):
    department = read_departments_table(db=db)
    if not department:
        raise HTTPException(status_code=404,detail=f"can't get departments table or does not exist")
    return department

@router.get('/truncate_table/')
def make_truncate(db: Session = Depends(get_db)):
    department = truncate_departments_table(db=db)
    if not department:
        raise HTTPException(status_code=404,detail=f"can't get departments table or does not exist")
    return department


@router.get('/make_backup/')
def make_backup(db: Session = Depends(get_db)):
    department = departments_table_backup(db=db)
    if not department:
        raise HTTPException(status_code=404,detail=f"can't get departments table or does not exist")
    return department


@router.get('/restore_table/')
def restore_table(db: Session = Depends(get_db)):
    department = departments_table_restore_backup(db=db)
    if not department:
        raise HTTPException(status_code=404,detail=f"can't get departments table or does not exist")
    return department

@router.get('/init_table/')
def init_table(db: Session = Depends(get_db)):
    obj = init_departments_table()
    create_multiple_deparments(request=obj,db=db)

    #DepartmentsCreate
    #department = create_multiple_deparments(db=db)
    #if not department:
    #    raise HTTPException(status_code=404,detail=f"can't get departments table or does not exist")
    #return department