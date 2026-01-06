import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
class StatutColis(str, enum.Enum):
    EN_ATTENTE = "en_attente"        
    EN_COURS = "en_cours"            
    LIVRE = "livre"                
    ANNULE = "annule" 


class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, nullable=False) 
    code_postal = Column(String, nullable=False)

class Colis(Base):
    __tablename__ = "colis"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    poids = Column(Float, nullable=False)
    ville_destination = Column(String, nullable=False)
    statut = Column(String, default=StatutColis.EN_ATTENTE)
    
    # Foreign Keys (Relationships)
    id_client = Column(Integer, ForeignKey("clients_expediteurs.id"), nullable=False)
    id_destinataire = Column(Integer, ForeignKey("destinataires.id"), nullable=False)
    id_zone = Column(Integer, ForeignKey("zones.id"), nullable=False)
    id_livreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True) # Nullable because it might not be assigned yet

    # ORM Relationships (Optional but helpful for code navigation)
    # zone = relationship("Zone")

class HistoriqueStatut(Base):
    __tablename__ = "historique_statut"

    id = Column(Integer, primary_key=True, index=True)
    id_colis = Column(Integer, ForeignKey("colis.id"), nullable=False)
    ancien_statut = Column(String, nullable=True)
    nouveau_statut = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    id_livreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True) 