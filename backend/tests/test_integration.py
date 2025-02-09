import requests

API_URL = "http://localhost:8000/fact-check"

def test_end_to_end_fact_check():
    claim = {"text": "Water boils at 100°C"}
    response = requests.post(API_URL, json=claim)

    assert response.status_code == 200
    data = response.json()
    
    assert "result" in data
    assert "evidence" in data
