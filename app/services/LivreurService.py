from ..repositories.LivreurRepository import LivreurRepository
from ..repositories.ZoneRepository import ZoneRepository 
from ..repositories.user_repository import  UserRepository
from ..schemas.livreur_schemas import LivreurCreate , LivreurAddZone
from ..models.user_models import Livreur , User
import smtplib
from email.message import EmailMessage
import uuid
from app.repositories.historique_repository import HistoriqueRepository
from app.repositories.colis_repository import ColisRepository
from app.services.email_service  import EmailNotification 
class LivreurService() :
    def __init__(self):
        self.livreur_repository = LivreurRepository()
        self.zone_repository = ZoneRepository()
        self.UserRepository = UserRepository()
        self.historique_repository  = HistoriqueRepository()
        self.colis = ColisRepository()
        self.email_notification = EmailNotification()
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
    def getall_Colis(self , user : User) :
        Livreur = self.UserRepository.get_by_id(user.id).livreur_profile
        return Livreur.colis
    def create_historique(self , historique) :
        colis = self.colis.get_by_id(historique.id_colis)
        historique = self.historique_repository.create(historique)
        self.email_notification.send_notification(colis)
        return historique

    
