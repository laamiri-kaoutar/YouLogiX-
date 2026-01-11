
from fastapi import APIRouter, HTTPException, status , Depends
from app.controllers.user_controller import UserController
from app.schemas.user_schemas import UserCreate, UserResponse
from app.api.deps import get_current_user , get_current_active_livreur 
from app.schemas.user_schemas import   UserUpdate 
from typing import Union
from app.models.user_models import User
from app.schemas.livreur_schemas import LivreurCreate  ,LivreurAddZone
from app.controllers.livreur_controller import LivreurController

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
    # user = get_current_user()
    return current_user
# @router.post("/profile")
# def user_profile(current_user :User = Depends(get_current_user) , user_data: Union[UserUpdate, LivreurUpdate]) :
#     usercontroller = UserController.updateProfile(user_data , current_user)
    
    



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
@router.get("/my_Colis")
def get_all_my_colis() :
    colis = LivreurController().getall_colis()
    return colis
# @router.get("/emailverification")/
# def emailverification() :
#      created_zone = Zone 

