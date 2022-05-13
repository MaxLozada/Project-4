"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_dashboard(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302


def test_auth_register(client):
    """This makes the index page"""
    response = client.get("/register")
    assert response.status_code == 200


def test_auth_login(client):
    """This makes the index page"""
    response = client.get("/login")
    assert response.status_code == 200


def test_auth_profile(client):
    """This makes the index page"""
    response = client.get("/profile")
    assert response.status_code == 200


def test_auth_account(client):
    """This makes the index page"""
    response = client.get("/account")
    assert response.status_code == 200
