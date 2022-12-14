from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.jobs import JobsCreate
from db.session import get_db
from db.repository.jobs import create_new_job,read_job_by_id,read_jobs_table,truncate_jobs_table,jobs_table_backup,jobs_table_restore_backup
from typing import List 
from utils.init_data import init_jobs_table
router = APIRouter()


@router.post('/')
def create_job(request : JobsCreate, db: Session = Depends(get_db)):
    job = create_new_job(input_job=request, db=db)
    return job


@router.post('/multiple')
def create_multiple_jobs(request : List[JobsCreate], db: Session = Depends(get_db)):
    if len(request) > 1000:
        raise HTTPException(status_code=409, detail="Exceed multiple's Jobs inserts simultaneusly")
    for job in request:
        new_job = create_new_job(input_job=job, db=db)
    return 'All jobs are created'

@router.get('/get/{id}')
def get_job_by_id(id:int, db: Session = Depends(get_db)):
    job = read_job_by_id(id,db=db)
    if not job:
        raise HTTPException(status_code=404,detail=f"job with this id {id} does not exist")
    return job

@router.get('/get_all/')
def get_all_jobs(db: Session = Depends(get_db)):
    job = read_jobs_table(db=db)
    if not job:
        raise HTTPException(status_code=404,detail=f"can't get jobs table or does not exist")
    return job

@router.get('/truncate_table/')
def make_truncate(db: Session = Depends(get_db)):
    job = truncate_jobs_table(db=db)
    if not job:
        raise HTTPException(status_code=404,detail=f"can't get jobs table or does not exist")
    return job


@router.get('/make_backup/')
def make_backup(db: Session = Depends(get_db)):
    job = jobs_table_backup(db=db)
    if not job:
        raise HTTPException(status_code=404,detail=f"can't get jobs table or does not exist")
    return job


@router.get('/restore_table/')
def restore_table(db: Session = Depends(get_db)):
    job = jobs_table_restore_backup(db=db)
    if not job:
        raise HTTPException(status_code=404,detail=f"can't get jobs table or does not exist")
    return job

@router.get('/init_table/')
def init_table(db: Session = Depends(get_db)):
    obj = init_jobs_table()
    create_multiple_jobs(request=obj,db=db)
    #print(obj)
    