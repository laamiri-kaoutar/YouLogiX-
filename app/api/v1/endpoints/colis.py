from fastapi import APIRouter, HTTPException
from app.schemas.colis_schemas import ColisCreate, ColisResponse , ColisUpdateStatus
from app.controllers.colis_controller import ColisController
from typing import List

router = APIRouter()

@router.post("/", response_model=ColisResponse)
def create_colis(colis: ColisCreate):

    controller = ColisController()
    result = controller.create(colis)
    
    return result

@router.patch('/{id}/status' , response_model= ColisResponse)
def update_status( id: int , update_data : ColisUpdateStatus) : 

    controller = ColisController()

    result = controller.update_status( id , update_data)

    if not result : 
        raise HTTPException(status_code=404, detail="Colis not found")
    
    return result

@router.get("/" , response_model= List[ColisResponse])
def read_all_colis():
    controller = ColisController()
    return controller.get_all()

@router.get("/{id}", response_model=ColisResponse)
def read_colis(id: int):
    controller = ColisController()
    colis = controller.get_by_id(id)
    
    if not colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return colis
