from ..repositories.LivreurRepository import LivreurRepository
from ..repositories.ZoneRepository import ZoneRepository
from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone
from ..models.user_models import Livreur
import smtplib
from email.message import EmailMessage
import uuid
class LivreurService() :
    def __init__(self):
        self.livreur_repository = LivreurRepository()
        self.zone_repository = ZoneRepository()
    def create(self , livreur : Livreur) :
        livreur  = self.livreur_repository.create(livreur)
        return livreur
    def update_zone(self , zone_name :LivreurAddZone  ) :
        livreur = self.livreur_repository.find_By_Id(1)
        zone_id =  self.zone_repository.find_By_name(zone_name.zone_name).id
        livreur.zone_id = zone_id
        return self.livreur_repository.update(livreur)
    def get_livreur(self) : 
        Livreur = self.livreur_repository.find_By_Id(1)
        return Livreur 
   
    def getall_Colis(self) :
        livreur = self.get_livreur()
        return livreur.colis_list
    
