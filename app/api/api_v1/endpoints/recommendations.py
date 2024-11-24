from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.recommendations import (
    AgricultureRecommendation,
    RecommendationRequest
)
from app.services.recommendation_engine import generate_recommendations
from app.core.config import settings

router = APIRouter()

@router.post("/analyze", response_model=List[AgricultureRecommendation])
async def get_recommendations(request: RecommendationRequest):
    """
    Gera recomendações personalizadas com base nos dados fornecidos.
    Integra dados climáticos, informações de culturas e análise de solo.
    """
    try:
        recommendations = await generate_recommendations(request)
        return recommendations
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao gerar recomendações: {str(e)}"
        )
