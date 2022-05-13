"""This test the map"""


def test_request_locations(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/locations"' in response.data


def test_request_locations_datatables(client):
    """This makes the index page"""
    response = client.get("/locations")
    assert response.status_code == 200
    assert b"locations" in response.data


