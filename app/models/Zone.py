from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship
from .user_models import Livreur
class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code_postal = Column(String, nullable=False, unique=True, index=True)
    users = relationship("Livreur", back_populates="zone")

