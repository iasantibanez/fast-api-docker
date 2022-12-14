from fastapi import FastAPI 
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
#from utils.init_data import

import logging 


#https://www.fastapitutorial.com/blog/fastapi-route/

def create_tables():
    logging.info("creating tables...")
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)
    logging.info('Loading routers...')

def insert_data_into_tables():
    logging.info('Data loaded')

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME
                    ,version=settings.PROJECT_NAME)
    #create_tables()
    #include_router(app)
    #insert_data_into_tables()


    @app.get('/')
    def hello():
        return 'Hello World!'

    return app


app = start_application()



