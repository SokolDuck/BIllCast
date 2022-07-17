from fastapi import APIRouter

from bill_cast.api.api_v1.endpoint import unit
from bill_cast.api.api_v1.endpoint import users
from bill_cast.api.api_v1.endpoint import login


api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(unit.router, prefix="/units", tags=["units"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
