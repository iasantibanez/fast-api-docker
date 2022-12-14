from fastapi import APIRouter

from apis.version1 import route_jobs
from apis.version1 import route_departments
from apis.version1 import route_employees



api_router = APIRouter()
api_router.include_router(route_jobs.router
                        ,prefix='/jobs'
                        ,tags=["jobs"])
api_router.include_router(route_departments.router
                        ,prefix='/deparments'
                        ,tags=["deparments"])
api_router.include_router(route_employees.router
                        ,prefix='/employees'
                        ,tags=["employees"])