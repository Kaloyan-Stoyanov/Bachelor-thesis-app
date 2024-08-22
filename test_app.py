import pytest
from flask import jsonify
from app import create_app
from app.simulation import devices

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home' in response.data

def test_iot_page(client):
    response = client.get('/iot')
    assert response.status_code == 200
    assert b'IoT Devices' in response.data

def test_manage_device_page(client):
    response = client.get('/manage/light1')
    assert response.status_code == 200
    assert b'Control Lights' in response.data

def test_toggle_device(client):
    device_id = 'light1'
    response = client.post(f'/toggle/{device_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['device_id'] == device_id
    assert data['status'] in ['on', 'off']
    
def test_get_device_status(client):
    device_id = 'light1'
    response = client.get(f'/status/{device_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] in ['on', 'off']
    
def test_set_device_temperature(client):
    device_id = 'thermostat1'
    response = client.post(f'/set-temperature/{device_id}', json={'temperature': 25})
    assert response.status_code == 200
    data = response.get_json()
    assert data['device_id'] == device_id
    assert data['temperature'] == 25
    
def test_get_device_stats(client):
    device_id = 'thermostat1'
    response = client.get(f'/get-stats/{device_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert 'status' in data
    assert 'toggle_count' in data
    assert 'temp_changes' in data
    
def test_invalid_device(client):
    response = client.get('/status/invalid_device')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'Device not found'

def test_set_invalid_temperature(client):
    device_id = 'thermostat1'
    response = client.post(f'/set-temperature/{device_id}', json={'temperature': 50})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Device not found or invalid temperature'
