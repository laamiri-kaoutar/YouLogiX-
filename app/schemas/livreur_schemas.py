from pydantic import BaseModel, ConfigDict
from typing import Optional
class LivreurCreate(BaseModel) :
    nom :str
    prenom : str
    telephone : str
    vehicule : str
class LivreurAddZone(BaseModel) :
    zone_name : str

    model_config = ConfigDict(from_attributes=True)


