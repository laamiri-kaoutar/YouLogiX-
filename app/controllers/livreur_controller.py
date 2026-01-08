

from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone
from ..services.LivreurService import LivreurService
from ..models.user_models import Livreur
class LivreurController() :
    def __init__(self):
        self.livreur_service = LivreurService() 
    def create(self,livreur :LivreurCreate): 
        # return livreur
   
        livreurobj = Livreur(**livreur.model_dump(mode="orm"))
        # return livreurobj
        obj_livreur = self.livreur_service.create(livreurobj)
        return obj_livreur 
    def add_zone_to_Livreur(self , livreur :LivreurAddZone) :
        return self.livreur_service.update_zone(livreur)
    def get_livreur(self) :
        return self.livreur_service.get_livreur() 

        


        

