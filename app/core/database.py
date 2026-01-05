from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 1. Create the Database Engine
# This opens the connection to Postgres using the URL from config
engine = create_engine(settings.DATABASE_URL)

# 2. Create the SessionLocal class
# We use this to create a temporary database session for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create the Base class
# All your future models (Colis, User) will inherit from this class
Base = declarative_base()

# 4. Dependency Injection
# This function will be used in every API route to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()