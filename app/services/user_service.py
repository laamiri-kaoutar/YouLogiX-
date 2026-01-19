from loguru import logger  # <--- Import Loguru
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate
from app.core.security import get_password_hash 
from app.services.LivreurService import LivreurService 
from app.services.ZoneService import ZoneService
from app.services.colis_service import ColisService
from app.models.user_models import User , Livreur
from app.models.colis_models import Zone
from app.services.email_service import EmailNotification
class UserService:
    def __init__(self):
        self.repo = UserRepository()
        self.livreurservice = LivreurService()
        self.zoneservice = ZoneService()
        self.colis_service = ColisService()
        self.emailnotification = EmailNotification()
        
    def create_user(self, user_data: UserCreate):
        logger.info(f"Attempting to create new user: {user_data.email}") # <--- Log entry

        # Check if email already exists
        if self.repo.get_by_email(user_data.email):
            logger.warning(f"Registration failed: Email {user_data.email} already exists") # <--- Log rejection
            return None 
        hashed_pwd = get_password_hash(user_data.password)
        data_dict = user_data.model_dump()
        del data_dict['password'] 
        data_dict['hashed_password'] = hashed_pwd

       
        new_user = self.repo.create(data_dict)
        
        
        logger.success(f"User created successfully with ID: {new_user.id}") # <--- Log success
        return new_user

    def get_user_by_id(self, id: int):
        logger.debug(f"Fetching user profile for ID: {id}") # <--- Log internal detail
        
        user = self.repo.get_by_id(id)
        
        if not user:
             logger.warning(f"User lookup failed: ID {id} not found")
             
        return user 
    def updateprofile(self , updated_data , current_user : User) : 
        allowed_users = ["admin" , "client"] 
        # return updated_data , current_user
        if current_user.role  in allowed_users : 
            self.repo.update(updated_data)
        else :
            # return updated_data
            livreur  = self.repo.get_by_email(current_user.email)
            # return livreur
            # return updated_data
            if livreur.livreur_profile is not None :
                livreur_obj = livreur
            else :
                livreur_obj = Livreur()

            # return livreur.livreur_profile
            if getattr(updated_data, "zone_name" , None):
                zone_id = self.zoneservice.find_by_name(Zone(name = updated_data.zone_name))
                if zone_id :
                   
                   livreur_obj.zone_id =  zone_id.id
            if getattr(updated_data, "vehicule" , None):
                 livreur_obj.vehicule = updated_data.vehicule
            livreur_obj.user_id = current_user.id

            # return livreur_obj
            return self.livreurservice.create(livreur_obj)
    def assign_livreur_to_colis(self ,data) :
        user = self.repo.get_by_email(data.email).livreur_profile
        colis = self.colis_service.get_colis_by_id(data.id)
        colis.id_livreur = user.id
        self.emailnotification.assign_livreuir(colis)
        return colis , colis.livreur

        
        

           
            
        
            