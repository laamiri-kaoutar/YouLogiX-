from fastapi import FastAPI, APIRouter, HTTPException, status , Depends
from app.schemas.zone_schemas import ZoneCreate , ZoneUpdate , ZoneResponse , ZoneSearchName , ZoneSearchCodePastal
from app.controllers.ZoneController import ZoneController
# from ..router import get_apirouter

from app.api.deps import get_current_active_livreur  , get_current_active_admin
from app.models.user_models import User


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_zone(zone_data: ZoneCreate, current_user: User = Depends(get_current_active_admin) ):
    created_zone = ZoneController().create(zone_data)
    return created_zone
@router.put("/update")
def update_zone(zone_data: ZoneUpdate):
    created_zone = ZoneController().update(zone_data)
    return created_zone
@router.get("/all")
def getall() :
    return ZoneController().show_all()
@router.delete("/delete")
def delete(zone : ZoneResponse) :
    zone = ZoneController().delete(zone)


@router.post("/search_name")
def SearchByName(zoneSearchname : ZoneSearchName  ) :
    zone = ZoneController().find_by_name(zoneSearchname)
    return zone
@router.post("/searchcodepostal")
def SearchByCOdePostal(zonecodepostal :ZoneSearchCodePastal) :
    zone = ZoneController().find_by_CodePostal(zonecodepostal)
    return zone


