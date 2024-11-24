from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CropInfo(BaseModel):
    name: str
    scientific_name: str
    description: str
    optimal_temperature: dict
    water_needs: dict
    soil_requirements: dict
    growth_cycle: dict
    planting_instructions: dict
    common_diseases: List[dict]
    nutrition_management: dict

class CropRecommendation(BaseModel):
    crop_name: str
    confidence_score: float
    optimal_planting_window: dict
    expected_yield: float
    risk_factors: List[dict]
    management_tips: List[str]

class CropMonitoring(BaseModel):
    date: datetime
    ndvi: float  # Normalized Difference Vegetation Index
    evi: float   # Enhanced Vegetation Index
    lai: float   # Leaf Area Index
    stage: str   # Current growth stage
    health_status: str
    stress_indicators: Optional[List[dict]]
    recommendations: Optional[List[str]]
