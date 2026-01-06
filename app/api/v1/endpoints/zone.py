from fastapi import FastAPI, APIRouter, HTTPException, status
from app.schemas.zone_schemas import ZoneCreate
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
app.include_router(router)
@app.get("/")
def root():

    return {"message": "Zones API is running"}

