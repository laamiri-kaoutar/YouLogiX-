from fastapi import APIRouter
from app.api.v1.endpoints import colis, users  , zone  , auth


api_router = APIRouter()


api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router( colis.router , prefix= "/colis" , tags=["colis"])

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"]) # <--- Add this


api_router.include_router(zone.router , prefix="/zones" , tags=["zones"])

