from fastapi import FastAPI, File, UploadFile
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
from utils.init_data import init_jobs_table,init_employees_table,init_departments_table

import logging 


#https://www.fastapitutorial.com/blog/fastapi-route/

def create_tables():
    logging.info("creating tables...")
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)
    logging.info('Loading routers...')

def insert_data_into_tables():
    init_jobs_table(settings.DATABASE_URL)
    init_departments_table(settings.DATABASE_URL)
    init_employees_table(settings.DATABASE_URL)
    logging.info('Data loaded')

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME
                    ,version=settings.PROJECT_NAME)
    create_tables()
    insert_data_into_tables()
    include_router(app)

    @app.get('/me')
    def hello():
        return 'Hello World! Im https://github.com/iasantibanez/ :)'

    return app


app = start_application()



