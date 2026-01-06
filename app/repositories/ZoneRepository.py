from ..models.Zone  import Zone
from sqlalchemy.orm import Session
from ..core.database import get_db
from sqlalchemy import select
from ..schemas.zone_schemas import ZoneCreate , ZoneUpdate
class ZoneRepository() :
    db : Session
    zone : Zone
    def __init__(self):
        self.db_generator = get_db()
        self.db = next(self.db_generator)
        self.zone = Zone()
    def create(self , zone : Zone ) :
        self.db.add(zone)
        self.db.commit()
        self.db.refresh(zone)
        return zone
    def find_By_Id(self , Zone_id : int) -> Zone :
        # return "ascascas"
        return self.db.query(Zone).filter(Zone.id == Zone_id).first()
        
    def find_By_name(self , Zone_name: str) -> Zone :
        return self.db.query(Zone).filter(Zone.name == Zone_name).first()
    def update(self , zone : ZoneUpdate) ->Zone : 
        zone_obj = self.db.get(Zone, zone.id)
        if not zone_obj:
            return None
        update_data = zone.model_dump(exclude={"id"}, exclude_unset=True)
        for key, value in update_data.items():
            setattr(zone_obj, key, value)
        self.db.commit()
        self.db.refresh(zone_obj)
        return zone_obj
    def delete (self , zone : Zone)  :
        self.db.delete(zone)
        self.db.commit()
    def getall(self) :
        return self.db.execute(select(Zone)).scalars().all()

        
        


    

        


    
        


        

