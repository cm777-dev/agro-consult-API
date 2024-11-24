from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Location(BaseModel):
    latitude: float
    longitude: float
    altitude: Optional[float]

class SoilData(BaseModel):
    type: str
    ph: float
    organic_matter: float
    nutrients: dict
    texture: str

class RecommendationRequest(BaseModel):
    location: Location
    soil_data: Optional[SoilData]
    target_crops: Optional[List[str]]
    planting_date: Optional[datetime]
    field_size: Optional[float]
    current_issues: Optional[List[str]]

class ManagementAction(BaseModel):
    action: str
    timing: str
    priority: str
    details: str
    expected_benefits: List[str]

class AgricultureRecommendation(BaseModel):
    timestamp: datetime
    location: Location
    recommended_crops: List[dict]
    climate_analysis: dict
    soil_recommendations: Optional[dict]
    management_actions: List[ManagementAction]
    risk_assessment: dict
    expected_outcomes: dict
    additional_notes: Optional[str]
