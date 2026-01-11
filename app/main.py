from fastapi import FastAPI
from loguru import logger 
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.router import api_router
from app.core.logging import configure_logging
from app.middlewares.authentication import authentication_middleware

from app.models import user_models, colis_models

configure_logging() 

logger.info("Starting YouLogix API initialization...") 

Base.metadata.create_all(bind=engine)
logger.success("Database tables verified/created successfully")

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.middleware("http")(authentication_middleware)

app.include_router(api_router , prefix=settings.API_V1_STR)
logger.info(f"API Router included with prefix: {settings.API_V1_STR}")



@app.get("/")
def root():
    logger.info("Root endpoint (Health Check) accessed") 
    return {"message": "Welcome to YouLogiX API", "status": "running"}