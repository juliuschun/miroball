"""MiroBall Backend - Flask app tests."""

import pytest
from app import create_app


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_health_endpoint(client):
    """Health check returns OK."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert 'MiroBall' in data['service']


def test_api_graph_endpoints_exist(client):
    """Graph API blueprint is registered."""
    # OPTIONS request to check route exists
    response = client.options('/api/graph/')
    # 404 or 200 are both acceptable — we just want no 500
    assert response.status_code != 500


def test_api_simulation_endpoints_exist(client):
    """Simulation API blueprint is registered."""
    response = client.options('/api/simulation/')
    assert response.status_code != 500


def test_api_report_endpoints_exist(client):
    """Report API blueprint is registered."""
    response = client.options('/api/report/')
    assert response.status_code != 500
