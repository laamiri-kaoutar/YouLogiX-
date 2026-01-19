
from fastapi import APIRouter, HTTPException, status , Depends
from app.controllers.user_controller import UserController
from app.schemas.user_schemas import UserCreate, UserResponse
from app.api.deps import get_current_user , get_current_active_client , get_current_active_livreur , get_current_active_admin
from app.schemas.user_schemas import   UserUpdate 
from typing import Union
from app.models.user_models import User
from app.schemas.livreur_schemas import LivreurCreate  ,LivreurAddZone , LivreurUpdate
from app.controllers.livreur_controller import LivreurController
from app.schemas.colis_schemas import ColisLivreur
from app.schemas.historique_schemas import HistoriqueCreate
from fastapi import Body
router = APIRouter()
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def Sign_Up(user: UserCreate):
    controller = UserController()
    new_user = controller.create(user)
    
    if not new_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
        
    return new_user
@router.get('current_user' , response_model=UserResponse )
def get_authenticated_user(current_user: User = Depends(get_current_user) ):
    return current_user
@router.get("/profile", response_model=Union[UserUpdate, LivreurUpdate])
async def get_profile(current_user = Depends(get_current_user)):
    return current_user
@router.post("/profile" )
def user_profile(user_data: Union[ LivreurUpdate] = Body(
        ...,
        openapi_examples={
            "livreur_update": {
                "summary": "Livreur Profile Update",
                "description": "Update fields for delivery personnel (livreurs)",
                "value": {
                    "nom": "Ahmed",
                    "prenom": "Ali",
                    "email": "ahmed@example.com",
                    "telephone": "+212611111111",
                    "vehicle": "Motorcycle",
                   
                    "zone_name": "casa"
                }
            }
        }
    ),
    current_user: User = Depends(get_current_user)
):
    user_controller = UserController()  # create an instance
    updated_user = user_controller.update_profile(user_data, current_user)
    return updated_user
    
    



@router.get("/{id}", response_model=UserResponse)
def read_user(id: int):
    controller = UserController()
    user = controller.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@router.get("/admin/colis")
def get_colis_Without_livreur(current_user :User =  Depends(get_current_user)) :
    colis  = UserController().get_colis_Without_livreur()
    return colis
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_Livreur(livreur: LivreurCreate ):
    created_zone = LivreurController().create(livreur)
    return created_zone
@router.post("/updatezone", status_code=status.HTTP_201_CREATED)
def asign_zone_to_colis(livreur: LivreurAddZone ) :
    created_zone = UserController().add_zone_to_Livreur(livreur)
    return created_zone
@router.post("admin/updatecolis", status_code=status.HTTP_201_CREATED)
def asign_livreur_to_colis(livreur: ColisLivreur  , current:User=Depends(get_current_active_admin)) :
    # return "AScas"
    created_zone = UserController().assign_livreur_to_colis(livreur)
    return created_zone

@router.get("/livreur", status_code=status.HTTP_201_CREATED)
def create_Livreur( ):
    created_zone = LivreurController().get_livreur()
    return created_zone
@router.post("/sendemil")
def send_email_Verification() : 
      created_zone = LivreurController().send_Emial()
      return created_zone
@router.get("/emailverification")
def emailverification() :
     created_zone = LivreurController().update_the_Status()
     return created_zone    
@router.post("/my_Colis")
def get_all_my_colis(current_user :User = Depends(get_current_active_livreur)) :
    # return "Ascascasc"
    # return current_user
    colis = LivreurController().getall_colis(current_user)
    return colis
@router.post("/historique_Colis")
def get_all_my_colis(historique:HistoriqueCreate) :
    historique = LivreurController().create_historique(historique)
    return "Created successfully"


