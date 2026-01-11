from app.services.user_service import UserService
from app.schemas.user_schemas import UserCreate
from app.controllers.colis_controller import ColisController 
from app.controllers.livreur_controller import LivreurController
from app.schemas.livreur_schemas import LivreurAddZone
class UserController:
    def __init__(self):
        self.service = UserService()
        self.colis_controller = ColisController()
        self.livreur_controller = LivreurController()
        
    def create(self, user_data: UserCreate):
        # Returns User object or None (if email exists)
        return self.service.create_user(user_data)

    def get_by_id(self, id: int):
        return self.service.get_user_by_id(id)
    def update_profile(self, update_data , current_user) :
        self.service.updateprofile(update_data , current_user)
    def get_colis_Without_livreur(self):
        return self.colis_controller.get_colis_without_livreur()
    def add_zone_to_Livreur(self , livreur :LivreurAddZone) :
        return self.livreur_controller.add_zone_to_Livreur(livreur)

