from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello from Jenkins Flask CI/CD!" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert b"Application is healthy" in response.data


def test_info():
    client = app.test_client()

    response = client.get("/info")

    assert response.status_code == 200
    assert b"Flask application deployed by Jenkins" in response.data

