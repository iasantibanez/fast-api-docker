import pandas as pd 
import requests
import json
import sys
import numpy as np
 
# setting path
sys.path.append('../FAST-API-2')

from schemas.jobs import JobsCreate
from schemas.employees import EmployeesCreate
from schemas.departments import DepartmentsCreate



def init_jobs_table():
    data = pd.read_csv(r'./src/data/jobs.csv',header=None)
    list_obj=[]
    for idx,row in data.iterrows():
        item = JobsCreate(id=row[0],job=row[1])
        list_obj.append(item)
    return list_obj

def init_employees_table():
    data = pd.read_csv(r'./src/data/hired_employees.csv',header=None)
    data = data.replace(np.nan, 0)
    list_obj=[]
    for idx,row in data.iterrows():
        #print(row[0],row[1],row[2],row[3],row[4])
        item = EmployeesCreate(id=row[0]
                            ,name=row[1]
                            ,datetime=row[2]
                            ,department_id= row[3]
                            ,job_id= row[4])
                
        list_obj.append(item)
    return list_obj

def init_departments_table():
    data = pd.read_csv(r'./src/data/departments.csv',header=None)
    list_obj=[]
    for idx,row in data.iterrows():
        item = DepartmentsCreate(id=row[0],department=row[1])
        list_obj.append(item)
    return list_obj
