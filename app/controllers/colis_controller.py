from app.services.colis_service import ColisService
from app.schemas.colis_schemas import ColisCreate
from app.models.colis_models import Colis
from app.schemas.colis_schemas import ColisUpdateStatus , ColisFilter


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
    

    def get_all(self, filters: ColisFilter):
        return self.service.get_all_colis(filters)


    def delete(self, id: int):
        return self.service.delete_colis(id)

    def get_for_client(self, id_client: int):
        return self.service.get_by_client(id_client)

    def get_for_livreur(self, id_livreur: int):
        return self.service.get_by_livreur(id_livreur)

    def get_for_destinataire(self, id_destinataire: int):
        return self.service.get_by_destinataire(id_destinataire)
    def get_colis_without_livreur(self) :
        self.service.get_colis_without_livreur()