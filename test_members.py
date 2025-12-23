from fastapi.testclient import TestClient
from app.main import app
from app.services.member_service import member_service

client = TestClient(app)

def test_create_member():
    response = client.post("/members/", json={"name": "John Doe", "email": "john@example.com", "membership_type": "standard"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data

def test_get_member():
    # Setup
    response = client.post("/members/", json={"name": "Jane Doe", "email": "jane@example.com"})
    member_id = response.json()["id"]

    # Test
    response = client.get(f"/members/{member_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_get_non_existent_member():
    response = client.get("/members/999")
    assert response.status_code == 404
