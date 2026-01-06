from ..services.ZoneService import ZoneService
from ..services.UserService import UserService
from ..models.Zone import Zone
from ..schemas.zone_schemas import ZoneCreate , ZoneUpdate , ZoneResponse
class ZoneController() :
    def __init__(self):
        self.ZoneService = ZoneService()
        self.userService = UserService()
    def create(self , zone : ZoneCreate )->Zone :
        zone = Zone(**zone.model_dump(mode="orm"))
        zone = self.ZoneService.create(zone)
        return zone
    def update (self, zone:ZoneUpdate) :
        zone = self.ZoneService.update(zone)
        return zone
    def show_all(self) :
        return self.ZoneService.getall()
    def delete(self , zone_schema : ZoneResponse) :
        return self.ZoneService.delete(zone_schema)

        
        
