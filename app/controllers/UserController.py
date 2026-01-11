
# from ..controllers import ZoneController
# from ..services import UserService
# class UserController() :
#     zonecontroller : ZoneController
#     userService : UserService
#     def __init__(self ):
#         self.zonecontroller = ZoneController()
#     def creat_zone(self) :

from ..controllers import ZoneController
from ..schemas.zone_schemas import LivreurCreate

from ..services import UserService
class UserController() :
    zonecontroller : ZoneController
    userService : UserService
    def __init__(self ):
        self.zonecontroller = ZoneController()
    # def creat_zone(self) :
    def get_colis_without_zone(self) :
        self



