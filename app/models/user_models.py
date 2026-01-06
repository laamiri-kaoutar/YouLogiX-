from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ClientExpediteur(Base):
    __tablename__ = "clients_expediteurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)

class Destinataire(Base):
    __tablename__ = "destinataires"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)

class Livreur(Base):
    __tablename__ = "livreurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    vehicule = Column(String, nullable=True) # e.g., "Moto", "Camion"
    # We will link the Zone later to avoid circular dependencies
    zone_id = Column(Integer, ForeignKey("zones.id"))
    zone = relationship("Zone", back_populates="users")