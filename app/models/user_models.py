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
    colis_list = relationship("Colis", back_populates="client")
class Destinataire(Base):
    __tablename__ = "destinataires"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)
    colis_list = relationship("Colis", back_populates="destinataire")
class Livreur(Base):
    __tablename__ = "livreurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    vehicule = Column(String, nullable=True)
    zone_id = Column(Integer, ForeignKey("zones.id"))
    zone = relationship("Zone", back_populates="livreurs")
    colis_list = relationship("Colis", back_populates="livreur")