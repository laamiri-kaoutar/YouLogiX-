from pydantic import BaseModel, ConfigDict
from typing import Optional

# Common fields
class ZoneBase(BaseModel):
    name: str
    code_postal: str

# Data required to CREATE
class ZoneCreate(ZoneBase):
    pass
# Data allowed to UPDATE (Everything optional)
class ZoneUpdate(BaseModel):
    nom: Optional[str] = None
    code_postal: Optional[str] = None
# Data returned in API RESPONSE
class ZoneResponse(ZoneBase) :
    id: int
    model_config = ConfigDict(from_attributes=True)