from fastapi import APIRouter
from app.api.v1.endpoints import colis, users  , zone
router =  APIRouter()
router.include_router(zone.router , prefix="/zones" , tags=["zones"])
router.include_router( colis.router , prefix= "/colis" , tags=["colis"])
router.include_router( users.router , prefix= "/livreurs" , tags=["livreurs"])
# api_router.include_router( users.router , prefix="/users" , tags=["users"])

