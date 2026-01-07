from fastapi import APIRouter
from app.api.v1.endpoints import colis, users  , zone


api_router = APIRouter()


api_router.include_router( colis.router , prefix= "/colis" , tags=["colis"])

# api_router.include_router( users.router , prefix="/users" , tags=["users"])

api_router.include_router(zone.router , prefix="/zones" , tags=["zones"])

