from sqlalchemy.orm import Session
from app.models.colis_models import Colis
from app.core.database import get_db

class ColisRepository:
    def __init__(self):
        self.db_generator = get_db()
        self.db = next(self.db_generator)

    def create(self, colis: Colis) -> Colis:
        self.db.add(colis)
        self.db.commit()
        self.db.refresh(colis)
        return colis
    
    def get_by_id(self , id : int) -> Colis:
        return self.db.query(Colis).filter(Colis.id == id).first()
    
    def update(self , colis: Colis) -> Colis :
        self.db.commit()
        self.db.refresh(colis)
        return colis 
    
    def get_all(self):
        return self.db.query(Colis).all()