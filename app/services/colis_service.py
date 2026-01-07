from app.repositories.colis_repository import ColisRepository
from app.repositories.historique_repository import HistoriqueRepository 

from app.models.colis_models import Colis , HistoriqueStatut

class ColisService:
    def __init__(self):
        # We initialize the Repository here
        self.repository = ColisRepository()
        self.history_repo = HistoriqueRepository()


    def create_colis(self, colis: Colis) -> Colis:
        # Later, we can add logic here (e.g., check if Zone is valid)
        return self.repository.create(colis)
    
    def update_status(self , id : int , new_status : str ,id_livreur : int = None ):

        colis = self.repository.get_by_id(id)

        if not colis :
            return None
        
        if colis.statut != new_status:
            history_entry = HistoriqueStatut(
                id_colis=colis.id,
                ancien_statut=colis.statut,
                nouveau_statut=new_status,
                id_livreur=id_livreur
            )
            self.history_repo.create(history_entry)

        
        colis.statut = new_status
        
        if id_livreur :
            colis.id_livreur = id_livreur
        
        return self.repository.update(colis)
    
    def get_all_colis(self):
        return self.repository.get_all()
    
    def get_colis_by_id(self , id : int):
        return self.repository.get_by_id(id)
    