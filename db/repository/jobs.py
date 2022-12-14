from sqlalchemy.orm import Session
from fastapi import  HTTPException
from schemas.jobs import JobsCreate
from db.models.jobs import Jobs
import logging
import pandas as pd 
from utils.avro import jobs_df_to_avro,jobs_avro_to_df

class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload





def create_new_job(input_job:JobsCreate,db=Session):
    new_job = Jobs(id=input_job.id,job=input_job.job)
    try:
        db.add(new_job)
        db.commit()
        db.refresh(new_job)
        #logging.info('Job Created Successfully')
        return f'Job: {new_job.job}, created Sucessfully' 
    except Exception as e:
        logging.error(f'Error at {e}', 'division', exc_info=e)
        raise HTTPException(status_code=409, detail="Job's duplicate key value violates unique constraint")
        #raise e.message
        # return f'Job: {new_job.job}, cant create' 
        #falta manejar casos en donde se rompe la regla de id unico.

def read_job_by_id(input_job:Jobs,db=Session):
    #print(input_job)
    job = db.query(Jobs).filter(Jobs.id == input_job).first()
    return job

def read_jobs_table(db=Session):
    #print(input_job)
    all_jobs = db.query(Jobs).all()
    return all_jobs


def jobs_table_backup(db=Session):
    all_jobs = db.query(Jobs).all()
    df = pd.DataFrame([t.__dict__ for t in all_jobs ]).reset_index(drop=True)
    df = df[['id','job']]
    jobs_df_to_avro(df)
    return all_jobs,'Table has been backed up'

def jobs_table_restore_backup(db=Session):
    truncate_jobs_table(db=db)
    df = jobs_avro_to_df()
    for idx,row in df.iterrows():
        job=JobsCreate(id=row.id,job=row.job)
        create_new_job(input_job=job,db=db)
    return 'Table has Restored'

def truncate_jobs_table(db=Session):
    try:
        affected_rows = db.query(Jobs).delete()
        if affected_rows == 0:
            db.commit()
            return 'Already empty Table'
        elif affected_rows > 0 :   
            db.commit()
            return f'number rows deleted: {affected_rows}'
       
    except Exception as e: #TO DO MANEJAR DEPENDENCIAS
        return f'{e}'