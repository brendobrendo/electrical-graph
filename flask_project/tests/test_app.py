import pytest
from app import app

def test_health_check():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_get_graph():
    client = app.test_client()
    response = client.get("/get_graph")
    assert response.status_code == 200
    assert response.get_json() == {"graph": "stub"}

def test_update_power():
    client = app.test_client()
    response = client.post("/update_power")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "updated_devices" in json_data
    for device in json_data["updated_devices"]:
        assert "device_id" in device
        assert "power_rating_watts" in device
        assert isinstance(device["power_rating_watts"], int)

def test_get_history():
    client = app.test_client()
    response = client.get("/get_history")
    assert response.status_code == 200
    assert response.get_json() == {"history": []}

def test_restore_snapshot():
    client = app.test_client()
    response = client.post("/restore_snapshot")
    assert response.status_code == 200
    assert response.get_json() == {"restored": "stub"}