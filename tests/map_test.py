"""This test the map"""


def test_request_locations(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/locations/map"' in response.data
    assert b'href="/locations_datatables"' in response.data


def test_request_locations_1(client):
    """This makes the index page"""
    response = client.get("/locations_datatables/")
    assert response.status_code == 200
    assert 302 == 200
    assert b"locations_datatables" in response.data


def test_request_locations_map(client):
    """This makes the index page"""
    response = client.get("/locations/map")
    assert response.status_code == 200
    assert b"locations/map" in response.data

