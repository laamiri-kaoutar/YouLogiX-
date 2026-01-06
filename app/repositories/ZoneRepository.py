from ..models.Zone  import Zone
from sqlalchemy.orm import Session
from ..core.database import get_db
from sqlalchemy import select
class ZoneRepository() :
    db : Session
    zone : Zone
    def __init__(self):
        self.db_generator = get_db()  # Store the generator
        self.db = next(self.db_generator)
        self.zone = Zone()

    def create(self , zone : Zone ) :
        self.db.add(zone)
        self.db.commit()
        self.db.refresh(zone)
        return zone
    def find_By_Id(self , Zone_id : int) ->Zone :
        zone_id =  self.db.get(self.zone , Zone)
        return zone_id
    def find_By_name(self , Zone_name: str) -> Zone :
        zone = select(Zone).where(Zone.name == Zone_name)
        return zone
    def update(self , zone : Zone) ->Zone :
        updated_Zone   =  self.create(zone)
        return updated_Zone
    def delete (self , zone : Zone)  : 
        self.db.delete(zone)
        


    

        


    
        


        

