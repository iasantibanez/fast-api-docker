from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from schemas.employees import EmployeesCreate
from db.session import get_db
from db.repository.employees import create_new_employee,read_employee_by_id,read_employees_table,truncate_employees_table,employees_table_backup,employees_table_restore_backup
from typing import List 
from utils.init_data import init_employees_table
router = APIRouter()


@router.post('/')
def create_employee(request : EmployeesCreate, db: Session = Depends(get_db)):
    employee = create_new_employee(input_employee=request, db=db)
    return employee

@router.post('/multiple')
def create_multiple_employees(request : List[EmployeesCreate], db: Session = Depends(get_db)):
    logs=[]
    if len(request) > 3000:
        raise HTTPException(status_code=409, detail="Exceed multiple's Employees inserts simultaneusly")
    #print(request)
    for employee in request:
        #print(employee)
        try:
            new_employee = create_new_employee(input_employee=employee, db=db)
        #break
        except:
            logs.append(f'employee: {employee.name} was not created') 
    return logs

@router.get('/get/{id}')
def get_employee_by_id(id:int, db: Session = Depends(get_db)):
    employee = read_employee_by_id(id,db=db)
    if not employee:
        raise HTTPException(status_code=404,detail=f"employee with this id {id} does not exist")
    return employee

@router.get('/get_all/')
def get_all_employees(db: Session = Depends(get_db)):
    employee = read_employees_table(db=db)
    if not employee:
        raise HTTPException(status_code=404,detail=f"can't get employees table or does not exist")
    return employee


@router.get('/truncate_table/')
def make_truncate(db: Session = Depends(get_db)):
    employees = truncate_employees_table(db=db)
    if not employees:
        raise HTTPException(status_code=404,detail=f"can't get employees table or does not exist")
    return employees



@router.get('/make_backup/')
def make_backup(db: Session = Depends(get_db)):
    employees = employees_table_backup(db=db)
    if not employees:
        raise HTTPException(status_code=404,detail=f"can't get employees table or does not exist")
    return employees


@router.get('/restore_table/')
def restore_table(db: Session = Depends(get_db)):
    employees = employees_table_restore_backup(db=db)
    if not employees:
        raise HTTPException(status_code=404,detail=f"can't get employees table or does not exist")

@router.get('/init_table/')
def init_table(db: Session = Depends(get_db)):
    obj = init_employees_table()
    #print(obj)
    response = create_multiple_employees(request=obj,db=db)

    return response