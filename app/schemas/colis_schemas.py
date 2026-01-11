from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, List
from datetime import datetime
from app.models.colis_models import StatutColis

# 1. Helper Schemas (For Nesting)
class ZoneResponse(BaseModel):
    id: int
    name: str
    code_postal: str
    model_config = ConfigDict(from_attributes=True)

class HistoriqueResponse(BaseModel):
    id: int
    ancien_statut: str
    nouveau_statut: str
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)


# 2. Base Schema 
class ColisBase(BaseModel):
    description: Optional[str] = None
    poids: float
    
    adresse_depart: str
    adresse_destination: str
    ville_destination: str

    destinataire_nom: str
    destinataire_telephone: str
    destinataire_email: Optional[EmailStr] = None
    
    id_zone: int
    
    id_client: Optional[int] = None 
    id_livreur: Optional[int] = None




# 3. Input Schema
class ColisCreate(ColisBase):
    pass


# 4. Filter Schema
class ColisFilter(BaseModel):
    statut: Optional[StatutColis] = None 
    id_zone: Optional[int] = None
    id_client: Optional[int] = None
    id_livreur: Optional[int] = None


class ColisSimpleResponse(ColisBase):
    id: int
    statut: str  
    # id_livreur: Optional[int] = None

    date_creation: datetime
    date_livraison: Optional[datetime] = None
    
    
    model_config = ConfigDict(from_attributes=True)

class ColisResponse(ColisSimpleResponse):
    zone: Optional[ZoneResponse] = None 
    historiques: List[HistoriqueResponse] = [] 

    model_config = ConfigDict(from_attributes=True)


class ColisUpdateStatus(BaseModel):
    statut: StatutColis
    id_livreur: Optional[int] = None

