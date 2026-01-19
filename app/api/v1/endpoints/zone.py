from fastapi import FastAPI, APIRouter, HTTPException, status , Depends , Request 
from app.schemas.zone_schemas import ZoneCreate , ZoneUpdate , ZoneResponse , ZoneSearchName , ZoneSearchCodePastal
from app.controllers.ZoneController import ZoneController
# <<<<<<< HEAD
# from ..router import get_apirouter

from app.api.deps import get_current_active_client  , get_current_active_admin , get_current_user
from app.models.user_models import User

from app.core.logging import logger

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_zone(zone_data: ZoneCreate, current_user: User = Depends(get_current_active_admin) ):
    logger.info("Creating a zone")

    created_zone = ZoneController().create(zone_data)
    return created_zone
@router.put("/update" )
def update_zone(zone_data: ZoneUpdate , current_user: User = Depends(get_current_active_admin)) :
    created_zone = ZoneController().update(zone_data)
    return created_zone
@router.get("/all")
def getall() :
    return ZoneController().show_all()
@router.delete("/delete")
def delete(zone : ZoneResponse , current_user: User = Depends(get_current_active_admin)) :
    zone = ZoneController().delete(zone)


@router.post("/search_name")
def SearchByName(zoneSearchname , current_user: User = Depends(get_current_user) ) :
    zone = ZoneController().find_by_name(zoneSearchname)
    return zone
@router.post("/searchcodepostal")
def SearchByCOdePostal(zonecodepostal :ZoneSearchCodePastal ,  current_user: User = Depends(get_current_user)) :
    zone = ZoneController().find_by_CodePostal(zonecodepostal)
    return zone


