from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.colis_models import HistoriqueStatut

class HistoriqueRepository:
    def __init__(self):
        self.db_generator = get_db()
        self.db = next(self.db_generator)

    def create(self, history: HistoriqueStatut) -> HistoriqueStatut:
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)
        return history