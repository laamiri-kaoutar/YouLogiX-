from ..repositories.ZoneRepository import ZoneRepository
from ..models import Zone
from ..schemas.zone_schemas import ZoneCreate , ZoneUpdate ,ZoneResponse
class ZoneService() :
    zonerepository : ZoneRepository
    def __init__(self):
        self.zonerepository = ZoneRepository()
    def create(self , zone : Zone ) ->Zone :
        zone = self.zonerepository.create(zone)
        return zone
    def update (self, zone : ZoneUpdate)  :
        existed_Zone = self.zonerepository.find_By_Id(zone.id)
        if existed_Zone :
            updated_zone  = self.zonerepository.update(zone)
            return updated_zone
    def delete(self , zone : ZoneResponse) :
        existed_zone = self.zonerepository.find_By_Id(zone.id)
        if existed_zone :
            self.zonerepository.delete(existed_zone)
            return "deleted Successfully!"
    def getall(self) :
        zones =  self.zonerepository.getall()
        if len(zones) == 0 :
            return {"message " : "no data exists" }
        return zones
