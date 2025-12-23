from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timedelta

client = TestClient(app)

def test_create_class():
    start_time = datetime.now() + timedelta(days=1)
    response = client.post("/classes/", json={
        "name": "Yoga",
        "instructor": "Alice",
        "capacity": 10,
        "start_time": start_time.isoformat(),
        "price": 20.0
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Yoga"
    assert data["current_occupancy"] == 0

def test_list_classes():
    response = client.get("/classes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
