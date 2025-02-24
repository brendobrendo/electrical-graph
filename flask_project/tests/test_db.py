import pytest
from db import add_device, get_device, get_db_session

def clear_device(device_id):
    with get_db_session() as session:
        session.run("MATCH (d:Device {device_id: $device_id}) DETACH DELETE d", device_id=device_id)

def test_add_and_get_device():
    device_id = "test-device"
    power_rating_watts = 100
    
    clear_device(device_id)  # Ensure no prior device with this ID exists
    add_device(device_id, power_rating_watts)
    result = get_device(device_id)
    
    assert result is not None
    assert result["d"]["device_id"] == device_id
    assert result["d"]["power_rating_watts"] == power_rating_watts
