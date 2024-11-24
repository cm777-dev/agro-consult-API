from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.middleware.rapidapi import RapidAPIMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    description="""
    Agro-Consult API provides agricultural consulting services through various endpoints.
    Features include:
    - Climate data and weather forecasts
    - Crop recommendations
    - Soil analysis
    - Agricultural management suggestions
    
    For support, contact: support@agroconsult.com
    """
)

# Set up RapidAPI middleware
app.add_middleware(RapidAPIMiddleware)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

@app.get("/")
async def root():
    return {
        "message": "Bem-vindo à API de Consultoria Agrícola",
        "version": settings.VERSION,
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
