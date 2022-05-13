"""This test the map"""


def test_request_locations(client):
    """This makes the index page"""
    response = client.get("/locations")
    assert response.status_code == 200
    assert b"locations" in response.data


def test_request_locations_upload(client):
    """This makes the index page"""
    response = client.get("/locations/upload")
    assert response.status_code == 200
    assert b"locations/upload" in response.data


def test_request_locations_upload(client):
    """This makes the index page"""
    response = client.get("/locations/new")
    assert response.status_code == 200
    assert b"locations/new" in response.data


def test_request_locations_map(client):
    """This makes the index page"""
    response = client.get("/locations/map")
    assert response.status_code == 200
    assert b"locations/map" in response.data

