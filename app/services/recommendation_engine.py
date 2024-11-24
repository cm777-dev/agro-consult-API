from app.schemas.recommendations import RecommendationRequest, AgricultureRecommendation
from app.core.config import settings
import httpx
from datetime import datetime
from typing import List
import asyncio

async def get_climate_data(location):
    """Obtém dados climáticos da ClimAPI"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.climapi.com/forecast",
            params={
                "lat": location.latitude,
                "lon": location.longitude,
                "days": 15
            },
            headers={"Authorization": f"Bearer {settings.CLIMAPI_KEY}"}
        )
        return response.json()

async def get_crop_data(location, soil_data=None):
    """Obtém recomendações de culturas da Agritec"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.agritec.com/recommendations",
            params={
                "lat": location.latitude,
                "lon": location.longitude,
                "soil_type": soil_data.type if soil_data else None
            },
            headers={"Authorization": f"Bearer {settings.AGRITEC_KEY}"}
        )
        return response.json()

async def get_vegetation_data(location):
    """Obtém dados de vegetação do SATVeg"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.satveg.com/analysis",
            params={
                "lat": location.latitude,
                "lon": location.longitude
            },
            headers={"Authorization": f"Bearer {settings.SATVEG_KEY}"}
        )
        return response.json()

async def analyze_risks(climate_data, crop_data, vegetation_data):
    """Analisa riscos com base nos dados coletados"""
    risks = {
        "climate": [],
        "soil": [],
        "pests": [],
        "market": []
    }
    
    # Análise climática
    for forecast in climate_data.get("daily_forecast", []):
        if forecast["conditions"]["precipitation"] > 50:
            risks["climate"].append({
                "type": "heavy_rain",
                "probability": 0.8,
                "impact": "high"
            })
    
    return risks

async def generate_recommendations(request: RecommendationRequest) -> List[AgricultureRecommendation]:
    """
    Gera recomendações agrícolas integrando múltiplas fontes de dados.
    """
    # Coleta dados em paralelo
    climate_data, crop_data, vegetation_data = await asyncio.gather(
        get_climate_data(request.location),
        get_crop_data(request.location, request.soil_data),
        get_vegetation_data(request.location)
    )
    
    # Analisa riscos
    risk_assessment = await analyze_risks(climate_data, crop_data, vegetation_data)
    
    # Gera recomendações de manejo
    management_actions = [
        {
            "action": "Irrigação",
            "timing": "Próximos 3 dias",
            "priority": "Alta" if risk_assessment["climate"] else "Normal",
            "details": "Ajustar irrigação com base na previsão de chuvas",
            "expected_benefits": ["Economia de água", "Prevenção de doenças"]
        }
    ]
    
    # Monta a recomendação final
    recommendation = AgricultureRecommendation(
        timestamp=datetime.now(),
        location=request.location,
        recommended_crops=crop_data.get("recommendations", []),
        climate_analysis={
            "forecast": climate_data.get("daily_forecast", []),
            "alerts": climate_data.get("alerts", [])
        },
        soil_recommendations={
            "corrections": [],
            "fertilization": []
        } if request.soil_data else None,
        management_actions=management_actions,
        risk_assessment=risk_assessment,
        expected_outcomes={
            "yield_potential": "high",
            "cost_efficiency": "medium",
            "sustainability_score": 8.5
        }
    )
    
    return [recommendation]
