from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class WeatherCondition(BaseModel):
    temperature: float
    humidity: float
    precipitation: float
    wind_speed: float
    description: str

class DailyForecast(BaseModel):
    date: datetime
    conditions: WeatherCondition
    sunrise: datetime
    sunset: datetime

class WeatherForecast(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    daily_forecast: List[DailyForecast]

class ClimateData(BaseModel):
    date: datetime
    temperature_max: float
    temperature_min: float
    temperature_avg: float
    precipitation: float
    humidity: float
    wind_speed: float
    solar_radiation: Optional[float]
