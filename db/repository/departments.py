from sqlalchemy.orm import Session
from fastapi import  HTTPException
from schemas.departments import DepartmentsCreate
from db.models.departments import Departments
from sqlmodel import select
import logging
import pandas as pd 
from utils.avro import departments_df_to_avro,departments_avro_to_df

def create_new_derpartment(input_department:DepartmentsCreate,db=Session):
    new_department = Departments(id=input_department.id,department=input_department.department)
    try:
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        #logging.info('Deparment Created Successfully')
        return f'Deparment: {new_department.department}, created Sucessfully' 
    except Exception as e:
        logging.error(f'Error at {e}', 'division', exc_info=e)
        raise HTTPException(status_code=409, detail="Deparment's duplicate key value violates unique constraint")


def read_department_by_id(department_id :Departments,db=Session):
    department = db.query(Departments).filter(Departments.id == department_id).first()
    return department

def read_departments_table(db=Session):
    all_departments = db.query(Departments).all()
    return all_departments

def departments_table_backup(db=Session):
    all_departments = db.query(Departments).all()
    df = pd.DataFrame([t.__dict__ for t in all_departments ]).reset_index(drop=True)
    df = df[['id','department']]
    departments_df_to_avro(df)
    return all_departments,'Table has been backed up'

def departments_table_restore_backup(db=Session):
    truncate_departments_table(db=db)
    df = departments_avro_to_df()
    for idx,row in df.iterrows():
        department=DepartmentsCreate(id=row.id,department=row.department)
        create_new_derpartment(input_department=department,db=db)
    return 'Table has Restored'

def truncate_departments_table(db=Session):
    try:
        affected_rows = db.query(Departments).delete()
        if affected_rows == 0:
            db.commit()
            return 'Already empty Table'
        elif affected_rows > 0 :   
            db.commit()
            return f'number rows deleted: {affected_rows}'
       
    except Exception as e: #TO DO MANEJAR DEPENDENCIAS
        return f'{e}'