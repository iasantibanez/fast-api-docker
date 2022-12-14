from sqlalchemy.orm import Session
from fastapi import  HTTPException
from schemas.employees import EmployeesCreate
from db.models.employees import Employees
import logging
import pandas as pd 
from utils.avro import employees_df_to_avro,employees_avro_to_df



def create_new_employee(input_employee:EmployeesCreate,db=Session):
    new_employee = Employees(id=input_employee.id
                            ,name=input_employee.name
                            ,datetime=input_employee.datetime
                            ,department_id=input_employee.department_id
                            ,job_id=input_employee.job_id)
    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return f'Employee: {new_employee.name}, created Sucessfully' 
    except Exception as e:
        logging.error(f'Error at {e}', 'division', exc_info=e)
        raise HTTPException(status_code=409, detail="Employee's duplicate key value violates unique constraint")

def read_employee_by_id(input_employee:Employees,db=Session):
    employee = db.query(Employees).filter(Employees.id == input_employee).first()
    return employee 

def read_employees_table(db=Session):
    all_employees = db.query(Employees).all()
    return all_employees


def employees_table_backup(db=Session):
    all_employees = db.query(Employees).all()
    df = pd.DataFrame([t.__dict__ for t in all_employees ]).reset_index(drop=True)
    df = df[['id','name','datetime','department_id','job_id']]
    employees_df_to_avro(df)
    return all_employees,'Table has been backed up'

def employees_table_restore_backup(db=Session):
    truncate_employees_table(db=db)
    df = employees_avro_to_df()
    for idx,row in df.iterrows():
        employee=EmployeesCreate(id=row['id']
                            ,name=row['name']
                            ,datetime=row['datetime']
                            ,department_id=row['department_id']
                            ,job_id=row['job_id'])
        create_new_employee(input_employee=employee,db=db)
    return 'Table has Restored'

def truncate_employees_table(db=Session):
    try:
        affected_rows = db.query(Employees).delete()
        if affected_rows == 0:
            db.commit()
            return 'Already empty Table'
        elif affected_rows > 0 :   
            db.commit()
            return f'number rows deleted: {affected_rows}'
       
    except Exception as e: #TO DO MANEJAR DEPENDENCIAS
        return f'{e}'
    