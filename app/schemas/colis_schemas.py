from pydantic import BaseModel, ConfigDict
from typing import Optional

# 1. Base Schema (Shared fields)
class ColisBase(BaseModel):
    description: Optional[str] = None
    poids: float
    ville_destination: str
    
    # The creator provides these IDs
    id_client: int
    id_destinataire: int
    id_zone: int

# 2. Input Schema (What the Client sends)
class ColisCreate(ColisBase):
    pass 

# 3. Output Schema (What the API replies)
class ColisResponse(ColisBase):
    id: int
    statut: str  
    id_livreur: Optional[int] = None
    
    model_config = ConfigDict(from_attributes=True)

