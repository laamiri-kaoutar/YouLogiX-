from sqlalchemy.orm import Session
from app.models.colis_models import Colis , Zone
from app.core.database import get_db
from sqlalchemy.orm import joinedload, selectinload 
from app.schemas.colis_schemas import ColisFilter 



class ColisRepository:
    def __init__(self):
        self.db_generator = get_db()
        self.db = next(self.db_generator)

    def create(self, colis: Colis) -> Colis:
        self.db.add(colis)
        self.db.commit()
        self.db.refresh(colis)
        return colis
    
    # def get_by_id(self , id : int) -> Colis:
    #     return self.db.query(Colis).filter(Colis.id == id).first()
    
    def update(self , colis: Colis) -> Colis :
        self.db.commit()
        self.db.refresh(colis)
        return colis 
    
   
    def get_all(self, filters: ColisFilter):
        query = self.db.query(Colis).options(
            joinedload(Colis.zone),
            selectinload(Colis.historiques)
        )

        if filters.statut:
            query = query.filter(Colis.statut == filters.statut)
        if filters.id_zone:
            query = query.filter(Colis.id_zone == filters.id_zone)
        if filters.id_client:
            query = query.filter(Colis.id_client == filters.id_client)
        if filters.id_livreur:
            query = query.filter(Colis.id_livreur == filters.id_livreur)
       
        return query.all()

 
    def get_by_id(self, id: int):
        return self.db.query(Colis).options(
            joinedload(Colis.zone),
            selectinload(Colis.historiques)
        ).filter(Colis.id == id).first()

    
    def delete(self, id: int) -> bool:
        colis = self.db.query(Colis).filter(Colis.id == id).first()
        if colis:
            self.db.delete(colis)
            self.db.commit()
            return True
        return False
    def get_colis_without_livreur(self):
        return (
        self.db.query(Colis)
        .filter(Colis.id_livreur.is_(None))
        .all()
    )