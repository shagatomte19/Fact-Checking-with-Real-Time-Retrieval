import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_fact_check_endpoint():
    response = client.post("/fact-check", json={"text": "The earth is flat"})
    assert response.status_code == 200
    assert "result" in response.json()
    assert "evidence" in response.json()

def test_past_fact_checks_endpoint():
    response = client.get("/past-fact-checks")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "claims" in response.json()
