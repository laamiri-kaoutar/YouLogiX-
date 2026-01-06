from ..services.ZoneService import ZoneService
from ..services.UserService import UserService
from ..models.Zone import Zone
from ..schemas.zone_schemas import ZoneCreate
class ZoneController() :
    zoneservice : ZoneService
    userService : UserService
    def __init__(self):
        self.ZoneService = ZoneService()
        self.userService = UserService()
    def create(self , zone : ZoneCreate )->Zone :
        zone = Zone(**zone.model_dump(mode="orm"))
        zone = self.ZoneService.create(zone)
        return zone

        
        
