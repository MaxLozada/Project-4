"""This test the map"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/locations"' in response.data
    assert b'href="/locations/map"' in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/locations")
    assert response.status_code == 200
    assert b"locations" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/locations/map")
    assert response.status_code == 200
    assert b"map" in response.data
