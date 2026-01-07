from ..services import ZoneService
from ..repositories import ZoneRepository
from ..models import Zone 
class UserService() :
    def __init__(self):
        self.zoneservice = ZoneService
        self.zonerepository = ZoneRepository
    def create(self, zone : Zone) :
        zone = self.zonerepository.create(zone)

        


