from ..models.user_models import Livreur
from sqlalchemy.orm import Session
from ..core.database import get_db
class LivreurRepository():
    db : Session
    def __init__(self):
        self.db_generator = get_db()
        self.db = next(self.db_generator)
    def create(self , livreur : Livreur) :
          self.db.add(livreur)
          self.db.commit()
          self.db.refresh(livreur)
          return livreur
    def update(self , livreur : Livreur ) :
        return self.create(livreur)
    def find_By_Id(self , livreur_id : int) :
        return self.db.query(Livreur).filter(Livreur.id == livreur_id).first()
    def delete(self  ) :
        pass 
    
   
         
