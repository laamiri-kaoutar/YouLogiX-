from pydantic import BaseModel, ConfigDict
from typing import Optional
class LivreurCreate(BaseModel) :
    nom :str    
    prenom : str
    telephone : str
    vehicule : str
    zone_name : str 
class LivreurAddZone(BaseModel) :
    zone_name : str 
    model_config = ConfigDict(from_attributes=True)
class LivreurUpdate(BaseModel) :
    vehicule : Optional[str] = None
    zone_name : Optional[str] = None



