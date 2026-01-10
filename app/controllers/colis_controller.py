from app.services.colis_service import ColisService
from app.schemas.colis_schemas import ColisCreate
from app.models.colis_models import Colis
from app.schemas.colis_schemas import ColisUpdateStatus


class ColisController:
    def __init__(self):
        self.service = ColisService()

    def create(self, colis_data: ColisCreate) -> Colis:

        colis_obj = Colis(**colis_data.model_dump())

        created_colis = self.service.create_colis(colis_obj)
        
        return created_colis
    
    def update_status(self, id : int, update_data : ColisUpdateStatus ):

        new_status = update_data.statut
        id_livreur = update_data.id_livreur
        updated_colis = self.service.update_status( id , new_status , id_livreur)
        return updated_colis
    def get_by_id(self , id: int):
        return self.service.get_colis_by_id(id)
    
    def get_all(self):
        return self.service.get_all_colis()