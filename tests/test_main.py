from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()

def test_docs_endpoint():
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_endpoint():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json()
    assert "paths" in response.json()

def test_climate_endpoint():
    response = client.get("/api/v1/climate/forecast")
    assert response.status_code in [200, 401, 403]  # 401/403 if authentication is required

def test_crops_endpoint():
    response = client.get("/api/v1/crops/list")
    assert response.status_code in [200, 401, 403]  # 401/403 if authentication is required

def test_recommendations_endpoint():
    response = client.get("/api/v1/recommendations/")
    assert response.status_code in [200, 401, 403]  # 401/403 if authentication is required
