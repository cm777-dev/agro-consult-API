from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.schemas.crops import CropInfo, CropRecommendation
from app.core.config import settings
import httpx

router = APIRouter()

@router.get("/info/{crop_name}", response_model=CropInfo)
async def get_crop_info(crop_name: str):
    """
    Obtém informações detalhadas sobre uma cultura específica.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.agritec.com/crops/{crop_name}",
                headers={"Authorization": f"Bearer {settings.AGRITEC_KEY}"}
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao obter informações da cultura: {str(e)}"
        )

@router.get("/recommendations", response_model=List[CropRecommendation])
async def get_crop_recommendations(
    latitude: float,
    longitude: float,
    soil_type: Optional[str] = None,
    season: Optional[str] = None
):
    """
    Obtém recomendações de culturas com base na localização e características do solo.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.agritec.com/recommendations",
                params={
                    "lat": latitude,
                    "lon": longitude,
                    "soil_type": soil_type,
                    "season": season
                },
                headers={"Authorization": f"Bearer {settings.AGRITEC_KEY}"}
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao obter recomendações: {str(e)}"
        )

@router.get("/monitoring/{latitude}/{longitude}", response_model=dict)
async def get_crop_monitoring(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str
):
    """
    Obtém dados de monitoramento de culturas via satélite usando o SATVeg.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.satveg.com/monitoring",
                params={
                    "lat": latitude,
                    "lon": longitude,
                    "start_date": start_date,
                    "end_date": end_date
                },
                headers={"Authorization": f"Bearer {settings.SATVEG_KEY}"}
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao obter dados de monitoramento: {str(e)}"
        )
