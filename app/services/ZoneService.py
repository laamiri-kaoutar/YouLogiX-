from ..repositories.ZoneRepository import ZoneRepository
from ..models import Zone

class ZoneService() :
    zonerepository : ZoneRepository
    def __init__(self):
        self.zonerepository = ZoneRepository()
    def create(self , zone : Zone ) ->Zone :
        zone = self.zonerepository.create(zone)
        return zone