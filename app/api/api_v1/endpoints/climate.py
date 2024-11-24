from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.schemas.climate import ClimateData, WeatherForecast
from app.core.config import settings
import httpx

router = APIRouter()

@router.get("/forecast/{latitude}/{longitude}", response_model=WeatherForecast)
async def get_weather_forecast(
    latitude: float,
    longitude: float,
    days: Optional[int] = 7
):
    """
    Obtém previsão do tempo para uma localização específica usando OpenWeatherMap.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.openweathermap.org/data/2.5/forecast",
                params={
                    "lat": latitude,
                    "lon": longitude,
                    "appid": settings.OPENWEATHER_API_KEY,
                    "units": "metric",
                    "cnt": days * 8  # OpenWeatherMap provides data in 3-hour steps
                }
            )
            response.raise_for_status()
            data = response.json()
            
            # Transform OpenWeatherMap data to our schema
            return {
                "latitude": latitude,
                "longitude": longitude,
                "timezone": data["city"]["timezone"],
                "daily_forecast": [
                    {
                        "date": item["dt"],
                        "conditions": {
                            "temperature": item["main"]["temp"],
                            "humidity": item["main"]["humidity"],
                            "precipitation": item["rain"]["3h"] if "rain" in item else 0,
                            "wind_speed": item["wind"]["speed"],
                            "description": item["weather"][0]["description"]
                        }
                    }
                    for item in data["list"]
                ]
            }
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao obter dados climáticos: {str(e)}"
        )

@router.get("/historical/{latitude}/{longitude}", response_model=List[ClimateData])
async def get_historical_data(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str
):
    """
    Obtém dados históricos do clima usando a NASA POWER API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://power.larc.nasa.gov/api/temporal/daily/point",
                params={
                    "parameters": "T2M,T2M_MAX,T2M_MIN,PRECTOT,RH2M,WS2M",
                    "community": "AG",
                    "longitude": longitude,
                    "latitude": latitude,
                    "start": start_date,
                    "end": end_date,
                    "format": "JSON"
                }
            )
            response.raise_for_status()
            data = response.json()
            
            # Transform NASA POWER data to our schema
            return [
                {
                    "date": date,
                    "temperature_max": values["T2M_MAX"],
                    "temperature_min": values["T2M_MIN"],
                    "temperature_avg": values["T2M"],
                    "precipitation": values["PRECTOT"],
                    "humidity": values["RH2M"],
                    "wind_speed": values["WS2M"],
                    "solar_radiation": None  # Could be added if needed
                }
                for date, values in data["properties"]["parameter"].items()
            ]
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao obter dados históricos: {str(e)}"
        )
