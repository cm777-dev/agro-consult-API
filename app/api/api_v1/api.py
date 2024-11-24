from fastapi import APIRouter
from app.api.api_v1.endpoints import climate, crops, soil, recommendations

api_router = APIRouter()

api_router.include_router(climate.router, prefix="/climate", tags=["climate"])
api_router.include_router(crops.router, prefix="/crops", tags=["crops"])
api_router.include_router(soil.router, prefix="/soil", tags=["soil"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
