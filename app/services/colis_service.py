from loguru import logger
from app.repositories.colis_repository import ColisRepository
from app.repositories.historique_repository import HistoriqueRepository 
from app.schemas.colis_schemas import ColisFilter
from app.models.colis_models import Colis , HistoriqueStatut

class ColisService:
    def __init__(self):
        self.repository = ColisRepository()
        self.history_repo = HistoriqueRepository()

    def create_colis(self, colis: Colis) -> Colis:
        logger.info(f"Creating new colis for client ID: {colis.id_client}")
        
        created_colis = self.repository.create(colis)
        
        logger.success(f"Colis created successfully with ID: {created_colis.id}")
        return created_colis
    
    def update_status(self , id : int , new_status : str ,id_livreur : int = None ):
        logger.info(f"Updating status for colis ID: {id} to '{new_status}'")
        
        colis = self.repository.get_by_id(id)

        if not colis :
            logger.warning(f"Update failed: Colis ID {id} not found")
            return None
        
        if colis.statut != new_status:
            logger.debug(f"Status change detected ({colis.statut} -> {new_status}). Recording history.")
            history_entry = HistoriqueStatut(
                id_colis=colis.id,
                ancien_statut=colis.statut,
                nouveau_statut=new_status,
            )
            self.history_repo.create(history_entry)

        colis.statut = new_status
        
        if id_livreur :
            logger.info(f"Assigning livreur ID {id_livreur} to colis {id}")
            colis.id_livreur = id_livreur
        
        updated_colis = self.repository.update(colis)
        logger.success(f"Colis ID {id} updated successfully")
        return updated_colis
    
    def get_colis_by_id(self, id):
        logger.debug(f"Fetching details for colis ID: {id}")
        return self.repository.get_by_id(id)

    def get_all_colis(self, filters: ColisFilter):
        logger.debug(f"Fetching colis list with filters: {filters}")
        return self.repository.get_all(filters)

    def delete_colis(self, id: int) -> bool:
        logger.info(f"Attempting to delete colis ID: {id}")
        
        colis = self.repository.get_by_id(id)
        if not colis:
            logger.warning(f"Delete failed: Colis ID {id} not found")
            return False

        self.history_repo.delete_by_colis_id(id)
        
        result = self.repository.delete(id)
        if result:
            logger.success(f"Colis ID {id} and associated history deleted")
            
        return result

    def get_by_client(self, client_id: int):
        logger.debug(f"Fetching colis for client ID: {client_id}")
        filters = ColisFilter(id_client=client_id)
        return self.repository.get_all(filters)

    def get_by_livreur(self, livreur_id: int):
        logger.debug(f"Fetching colis for livreur ID: {livreur_id}")
        filters = ColisFilter(id_livreur=livreur_id)
        return self.repository.get_all(filters)
