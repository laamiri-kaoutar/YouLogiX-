from fastapi import APIRouter
from app.api.v1.endpoints import colis, users  , zone


def get_apirouter() :
    router = APIRouter()
    return router
router = get_apirouter()
router.include_router(zone.router , prefix="/zones" , tags=["zones"])
