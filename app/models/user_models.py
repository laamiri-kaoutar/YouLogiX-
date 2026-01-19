from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class Role(str, enum.Enum):
    CLIENT = "client"
    LIVREUR = "livreur"
    ADMIN = "admin"
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=False)
    role = Column(String, default=Role.CLIENT)
    hashed_password = Column(String, nullable=False)
    colis = relationship("Colis" ,back_populates="user" ,uselist=False )
    livreur_profile = relationship("Livreur", back_populates="user", uselist=False)
class Livreur(Base):
    __tablename__ = "livreurs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vehicule = Column(String, nullable=True) 
    zone_id = Column(Integer, ForeignKey("zones.id"))
    colis = relationship("Colis" , back_populates="User")
    zone = relationship("Zone", back_populates="livreur")
    user = relationship("User", back_populates="livreur_profile")
    colis = relationship("Colis", back_populates="livreur")