from fastapi import FastAPI, APIRouter, HTTPException, status
from app.schemas.livreur_schemas import LivreurCreate  ,LivreurAddZone
from app.controllers.livreur_controller import LivreurController
router = APIRouter()
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_Livreur(livreur: LivreurCreate):
    created_zone = LivreurController().create(livreur)
    return created_zone
@router.post("/updatezone", status_code=status.HTTP_201_CREATED)
def create_Livreur(livreur: LivreurAddZone ):
    created_zone = LivreurController().add_zone_to_Livreur(livreur)
    return created_zone
@router.get("/livreur", status_code=status.HTTP_201_CREATED)
def create_Livreur( ):
    created_zone = LivreurController().get_livreur()
    return created_zone
