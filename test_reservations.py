from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timedelta

client = TestClient(app)

def test_full_reservation_flow():
    # 1. Create Member
    m_resp = client.post("/members/", json={"name": "Bob", "email": "bob@example.com", "membership_type": "standard"})
    member_id = m_resp.json()["id"]

    # 2. Create Class
    c_resp = client.post("/classes/", json={
        "name": "Spinning",
        "instructor": "Charlie",
        "capacity": 1, # Small capacity to test limit
        "start_time": (datetime.now() + timedelta(days=1)).isoformat(),
        "price": 50.0
    })
    class_id = c_resp.json()["id"]

    # 3. Reserve (Success)
    r_resp = client.post("/reservations/", json={"member_id": member_id, "class_id": class_id})
    assert r_resp.status_code == 201
    assert r_resp.json()["status"] == "confirmed"

    # 4. Reserve (Fail - Capacity)
    m2_resp = client.post("/members/", json={"name": "Dave", "email": "dave@example.com", "membership_type": "standard"})
    member2_id = m2_resp.json()["id"]
    
    r_fail = client.post("/reservations/", json={"member_id": member2_id, "class_id": class_id})
    assert r_fail.status_code == 400
    assert "full" in r_fail.json()["detail"]

    # 5. Cancel
    res_id = r_resp.json()["id"]
    c_cancel = client.delete(f"/reservations/{res_id}")
    assert c_cancel.status_code == 204
    
    # 6. Reserve Again (Success)
    r_retry = client.post("/reservations/", json={"member_id": member2_id, "class_id": class_id})
    assert r_retry.status_code == 201
