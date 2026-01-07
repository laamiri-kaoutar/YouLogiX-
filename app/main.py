from fastapi import APIRouter ,FastAPI
from .api.v1 import router
app = FastAPI( 
    title="YouLogiX Zones API",
    description="Zones Management",
    version="1.0.0"
)
app.include_router(router.router)