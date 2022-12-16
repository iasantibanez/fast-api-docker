import pandas as pd 
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
 
# setting path
sys.path.append('../FAST-API-2')

from schemas.jobs import JobsCreate
from schemas.employees import EmployeesCreate
from schemas.departments import DepartmentsCreate



def init_jobs_table(db_url):
    db = create_engine(db_url)
    conn = db.connect()
    data = pd.read_csv(r'./src/data/jobs.csv',names=['id','job_id']).set_index('id')
    response=''
    try:
        #pass
        response=data.to_sql('jobs', conn,if_exists= 'replace')
        print(f'data jobs Inserted Rows Inserted: {len(data)}')
    except Exception as e:
        print(e)
    #conn.commit()
    conn.close()
    return f"Data Inserted: {response}"

def init_employees_table(db_url):
    db = create_engine(db_url)
    conn = db.connect()
    data = pd.read_csv(r'./src/data/hired_employees.csv',names=['id','name','datetime','department_id','job_id']).set_index('id')
    response=''
    try:
        #pass
        response=data.to_sql('employees', conn,if_exists= 'replace')
        print(f'data hired_employees Rows Inserted: {len(data)}')
    except Exception as e:
        print(e)
    #conn.commit()
    conn.close()
    return f"Data Inserted: {response}"

def init_departments_table(db_url):
    db = create_engine(db_url)
    conn = db.connect()
    data = pd.read_csv(r'./src/data/departments.csv',names=['id','department_id']).set_index('id')
    response=''
    try:
        #pass
        response=data.to_sql('departments', conn,if_exists= 'replace')
        print(f'data departments Rows Inserted: {len(data)}')
    except Exception as e:
        print(e)
    #conn.commit()
    conn.close()
    return f"Data Inserted: {response}"