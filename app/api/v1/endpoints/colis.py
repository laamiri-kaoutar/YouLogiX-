from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.colis_schemas import ColisCreate, ColisResponse , ColisSimpleResponse , ColisUpdateStatus , ColisFilter
from app.controllers.colis_controller import ColisController
from typing import List
from app.api.deps import get_current_user , get_current_active_livreur 
from app.models.user_models import User , Role



router = APIRouter()

@router.post("/", response_model=ColisSimpleResponse)
def create_colis(colis: ColisCreate):
   
    controller = ColisController()
    result = controller.create(colis)
    return result

# @router.post("/", response_model=ColisSimpleResponse)
# def create_colis(
#     colis: ColisCreate, 
#     current_user: User = Depends(get_current_user) 
# ):
#     colis.id_client = current_user.id 

#     controller = ColisController()
#     result = controller.create(colis)
#     return result


@router.patch('/{id}/status', response_model=ColisSimpleResponse)
def update_status(
    id: int, 
    update_data: ColisUpdateStatus,
    current_user: User = Depends(get_current_active_livreur) 
):
    controller = ColisController()
    if current_user.role == Role.LIVREUR :
       print(current_user)
       update_data.id_livreur = current_user.id 

    result = controller.update_status(id, update_data)
    # print(User.role)


    if not result:
        raise HTTPException(status_code=404, detail="Colis not found")
    
    return result



@router.get("/{id}", response_model=ColisResponse)
def read_colis(id: int):
    controller = ColisController()
    colis = controller.get_by_id(id)
    
    if not colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return colis

@router.get("/", response_model=List[ColisResponse])
def read_all_colis(filters: ColisFilter = Depends() ):
    controller = ColisController()
    return controller.get_all(filters)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_colis(id: int):
    controller = ColisController()
    success = controller.delete(id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Colis not found")
    return

@router.get("/client/{id_client}", response_model=List[ColisResponse])
def get_colis_client(id_client: int):
    controller = ColisController()
    return controller.get_for_client(id_client)

@router.get("/livreur/{id_livreur}", response_model=List[ColisResponse])
def get_colis_livreur(id_livreur: int):
    controller = ColisController()
    return controller.get_for_livreur(id_livreur)
