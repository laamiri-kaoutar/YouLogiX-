from ..controllers import ZoneController
from ..services import UserService
class UserController() :
    zonecontroller : ZoneController
    userService : UserService
    def __init__(self ):
        self.zonecontroller = ZoneController()
    def creat_zone(self) :
