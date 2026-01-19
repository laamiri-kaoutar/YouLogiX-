from pydantic import BaseModel, ConfigDict
from typing import Optional
class HistoriqueCreate(BaseModel) :
    id_colis :int
    nouveau_statut : str
