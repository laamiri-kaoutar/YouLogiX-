from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.router import router

# --- IMPORT MODELS HERE TO REGISTER THEM WITH SQLALCHEMY ---
from app.models import user_models, colis_models
# -----------------------------------------------------------

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(router , prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to YouLogiX API", "status": "running"}

