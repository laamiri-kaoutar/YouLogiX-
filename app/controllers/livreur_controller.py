

from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone
from ..services.LivreurService import LivreurService
from ..models.user_models import Livreur
from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone
from app.models.user_models import User
from app.services.email_service import EmailNotification
from app.schemas.historique_schemas import HistoriqueCreate
from app.models.colis_models import HistoriqueStatut
class LivreurController() :
    static = 0
    def __init__(self):
        self.livreur_service = LivreurService() 
        self.emil_notification = EmailNotification()
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
    def getall_colis(self , user:User) :
        colis = self.livreur_service.getall_Colis(user)
        return colis
    def livred_colis(self , ) :
        self.livreur_service.create_history()
    def create_historique(self , historique : HistoriqueCreate ) :
        historique_obj = HistoriqueStatut(**historique.model_dump(mode="orm"))
        historique_obj.ancien_statut = "an cours" 
        
        self.livreur_service.create_historique(historique_obj)
   
        
        
    


        


        

