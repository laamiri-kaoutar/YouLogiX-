from fastapi import APIRouter
<<<<<<< HEAD
from app.api.v1.endpoints import colis, users  , zone


def get_apirouter() :
    router = APIRouter()
    return router
router = get_apirouter()
router.include_router(zone.router , prefix="/zones" , tags=["zones"])
=======
from app.api.v1.endpoints import colis , users

api_router = APIRouter()


api_router.include_router( colis.router , prefix= "/colis" , tags=["colis"])

# api_router.include_router( users.router , prefix="/users" , tags=["users"])
>>>>>>> f9b4f542ba9f46a95f990e80ee591ad09d21ae17
