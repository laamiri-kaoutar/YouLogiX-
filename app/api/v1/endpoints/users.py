from fastapi import APIRouter, HTTPException, status , Depends
from app.controllers.user_controller import UserController
from app.schemas.user_schemas import UserCreate, UserResponse
from app.api.deps import get_current_user , get_current_active_livreur 
from app.schemas.user_schemas import LivreurUpdate , UserUpdate 
from typing import Union
from app.models.user_models import User

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
@router.post("/profile")
def user_profile(current_user :User = Depends(get_current_user) , user_data: Union[UserUpdate, LivreurUpdate]) :
    usercontroller = UserController.updateProfile(user_data , current_user)
    
    



@router.get("/{id}", response_model=UserResponse)
def read_user(id: int):
    controller = UserController()
    user = controller.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user