from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_profile():
    r = client.get("/api/profile")
    assert r.status_code == 200
    data = r.json()
    assert "name" in data and "title" in data and "bio" in data

def test_update_profile():
    payload = {"name": "Test", "title": "T", "bio": "B"}
    r = client.put("/api/profile", json=payload)
    assert r.status_code == 200
    assert r.json()["ok"] is True

    r2 = client.get("/api/profile")
    assert r2.json()["name"] == "Test"
