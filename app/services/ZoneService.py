from ..repositories.ZoneRepository import ZoneRepository
from ..models import Zone

class ZoneService() :
    zonerepository : ZoneRepository
    def __init__(self):
        self.zonerepository = ZoneRepository()
    def create(self , zone : Zone ) ->Zone :
        zone = self.zonerepository.create(zone)
        return zone
    def update (self, zone :Zone)  :
        existed_Zone = self.zonerepository.find_By_Id(zone.id)
        updated_zone  = self.zonerepository.update(existed_Zone)
    def delete(self , zone :Zone) :
        existed_zone = self.zonerepository.find_By_Id(Zone.id)
        self.zonerepository.delete(existed_zone)
        
