

from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone
from ..services.LivreurService import LivreurService
from ..models.user_models import Livreur
from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone

class LivreurController() :
    static = 0
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
    def send_Emial(self) :
        return self.livreur_service.send_email_notification()
    def update_the_Status(self) :
        LivreurController.static +=1   
        return LivreurController.static
    def getall_colis(self) :
        self.livreur_service.getall_Colis()


        


        

