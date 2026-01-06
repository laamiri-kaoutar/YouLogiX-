from ..models import Zone
from sqlalchemy.orm import Session
from ..core.database import get_db
class ZoneRepository() :
    db : Session
    def __init__(self):
        self.db_generator = get_db()  # Store the generator
        self.db = next(self.db_generator)
    def create(self , zone : Zone ) :
        self.db.add(zone)
        self.db.commit()
        self.db.refresh(zone)
        return zone

        

