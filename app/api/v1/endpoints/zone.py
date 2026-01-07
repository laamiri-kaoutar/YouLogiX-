from fastapi import FastAPI, APIRouter, HTTPException, status
from app.schemas.zone_schemas import ZoneCreate , ZoneUpdate , ZoneResponse , ZoneSearchName , ZoneSearchCodePastal
from app.controllers.ZoneController import ZoneController

app = FastAPI(
    title="YouLogiX Zones API",
    description="Zones Management",
    version="1.0.0"
)

router = APIRouter(prefix="/users/zones", tags=["Zones"])
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_zone(zone_data: ZoneCreate):
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
app.include_router(router)
@router.post("/search_name")
def SearchByName(zoneSearchname : ZoneSearchName  ) :
    zone = ZoneController().find_by_name(zoneSearchname)
    return zone
@router.post("/searchcodepostal")
def SearchByCOdePostal(zonecodepostal :ZoneSearchCodePastal) :
    zone = ZoneController().find_by_CodePostal(zonecodepostal)
    return zone
app.include_router(router)
@app.get("/")
def root():
    return {"message": "Zones API is running"}

