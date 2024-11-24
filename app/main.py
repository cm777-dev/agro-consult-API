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
    🌾 Agro-Consult API - Your Agricultural Intelligence Platform

    This API provides comprehensive agricultural consulting services through various endpoints, helping farmers and agricultural professionals make data-driven decisions.

    ## Features

    ### 🌡️ Climate Analysis
    - Get detailed weather forecasts for agricultural regions
    - Access historical climate data
    - Receive weather alerts for adverse conditions

    ### 🌱 Crop Management
    - Get crop recommendations based on soil and climate conditions
    - Access detailed crop information and best practices
    - Receive planting and harvesting timing suggestions

    ### 🚜 Agricultural Recommendations
    - Get personalized farming recommendations
    - Access soil management suggestions
    - Receive pest and disease control advice

    ## Authentication
    This API uses RapidAPI for authentication. You need to:
    1. Subscribe to the API on RapidAPI
    2. Use your RapidAPI key in the X-RapidAPI-Key header
    3. Include X-RapidAPI-Host header in your requests

    ## Rate Limits
    - Free Tier: 100 requests/day
    - Pro Tier: 10,000 requests/day
    - Enterprise Tier: Custom limits

    For support or questions, contact: support@agroconsult.com
    """,
    terms_of_service="https://rapidapi.com/cm777-dev/api/agro-consult-api/terms",
    contact={
        "name": "API Support",
        "url": "https://github.com/cm777-dev/agro-consult-API/issues",
        "email": "support@agroconsult.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/cm777-dev/agro-consult-API/blob/main/LICENSE",
    },
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

@app.get("/", tags=["Status"])
async def root():
    """
    Get API status and version information.
    
    Returns:
        dict: Basic information about the API including version and documentation URLs.
    
    Example:
        ```python
        import requests
        import os
        
        headers = {
            'X-RapidAPI-Key': os.getenv('RAPIDAPI_KEY'),
            'X-RapidAPI-Host': 'agro-consult-api.p.rapidapi.com'
        }
        
        response = requests.get("https://agro-consult-api.p.rapidapi.com/", headers=headers)
        print(response.json())
        ```
    """
    return {
        "message": "Bem-vindo à API de Consultoria Agrícola",
        "version": settings.VERSION,
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "status": "operational",
        "github_url": "https://github.com/cm777-dev/agro-consult-API"
    }
