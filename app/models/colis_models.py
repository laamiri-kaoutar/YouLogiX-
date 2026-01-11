import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text , Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum

class StatutColis(str, enum.Enum):
    EN_ATTENTE = "en_attente"        
    EN_COURS = "en_cours"            
    LIVRE = "livre"                
    ANNULE = "annule" 



class Zone(Base):
    __tablename__ = "zones"
    table_args = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code_postal = Column(String, nullable=False, unique=True, index=True)
    users = relationship("Livreur", back_populates="zone")


class Colis(Base):
    __tablename__ = "colis"    
    id = Column(Integer, primary_key=True, index=True)
    
    description = Column(Text, nullable=True) 
    poids = Column(Float, nullable=False)
    
    adresse_depart = Column(String, nullable=False)
    
    adresse_destination = Column(String, nullable=False)
    ville_destination = Column(String, nullable=False) 
    
    destinataire_nom = Column(String, nullable=False)       
    destinataire_telephone = Column(String, nullable=False) 
    destinataire_email = Column(String, nullable=True)      
    
    statut = Column(String, default=StatutColis.EN_ATTENTE)
    date_creation = Column(DateTime(timezone=True), server_default=func.now())
    date_livraison = Column(DateTime(timezone=True), nullable=True) # Set this when status becomes LIVRE
    
    id_client = Column(Integer, ForeignKey("users.id"), nullable=False)
    id_livreur = Column(Integer, ForeignKey("users.id"), nullable=True) 
    id_zone = Column(Integer, ForeignKey("zones.id"), nullable=False)

    zone = relationship("Zone")
    historiques = relationship("HistoriqueStatut", back_populates="colis", cascade="all, delete-orphan")

    # client = relationship("User", foreign_keys=[id_client])
    # livreur = relationship("User", foreign_keys=[id_livreur])



# class Colis(Base):
#     __tablename__ = "colis"

#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String, nullable=True)
#     poids = Column(Float, nullable=False)
    
#     adresse_depart = Column(String, nullable=False) 

#     adresse_destination = Column(String, nullable=False)
#     ville_destination = Column(String, nullable=False) 
    
#     destinataire_email = Column(String, nullable=False)
    
#     statut = Column(String, default=StatutColis.EN_ATTENTE)
    
#     # Foreign Keys
#     id_client = Column(Integer, ForeignKey("users.id"), nullable=False)
#     id_zone = Column(Integer, ForeignKey("zones.id"), nullable=False)
#     id_livreur = Column(Integer, ForeignKey("users.id"), nullable=True) 

#     # Relationships
#     zone = relationship("Zone")
#     # client = relationship("User", foreign_keys=[id_client])
#     # livreur = relationship("User", foreign_keys=[id_livreur])
#     historiques = relationship("HistoriqueStatut", back_populates="colis")

    # # Foreign Keys
    # id_client = Column(Integer, ForeignKey("clients_expediteurs.id"), nullable=False)
    # id_destinataire = Column(Integer, ForeignKey("destinataires.id"), nullable=False)
    # id_zone = Column(Integer, ForeignKey("zones.id"), nullable=False)
    # id_livreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True)
    
    # # Relationships - use string references
    # client = relationship("ClientExpediteur", back_populates="colis_list")
    # destinataire = relationship("Destinataire", back_populates="colis_list")
    # zone = relationship("Zone", back_populates="colis_list")
    # livreur = relationship("Livreur", back_populates="colis_list") # Nullable because it might not be assigned yet
    # # ORM Relationships (Optional but helpful for code navigation)
    # # zone = relationship("Zone")
class HistoriqueStatut(Base):
    __tablename__ = "historique_statut"

    id = Column(Integer, primary_key=True, index=True)
    id_colis = Column(Integer, ForeignKey("colis.id"), nullable=False)
    ancien_statut = Column(String, nullable=True)
    nouveau_statut = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    # id_livreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True) 

    colis = relationship("Colis", back_populates="historiques")
