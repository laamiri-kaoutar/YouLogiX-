from app.models.user_models import Role
from pydantic import BaseModel
class Client_Create(BaseModel):
    name : str 
    role : Role 
    email : str 
    password :str
    telephone : str


