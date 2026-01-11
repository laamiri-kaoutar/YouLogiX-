from pydantic import BaseModel, EmailStr, ConfigDict , Field
from typing import Optional
from app.models.user_models import Role

class UserBase(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    role: Role = Role.CLIENT

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)

    # password: str 

class UserUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    password: Optional[str] = None 
class LivreurUpdate() :

class UserResponse(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)