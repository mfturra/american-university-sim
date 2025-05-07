# modify Python's sys runtime env
import sys
# interact with OS
import os

# add parent directory to sys path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from course import create_app, db
from config import TestConfig

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app(TestConfig)
    
    # Create a test context
    with app.app_context():
        # Create tables
        db.create_all()
        yield app
        # Clean up after test
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client for app with setup and tear down logic."""
    return app.test_client()

#-----Home Routing to Login & Signup Endpoints
def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome Young Grasshopper!" in response.data 

def test_login_post(client):
    """Test posting to login route."""
    response = client.post('/', data={'command': 'login'}, follow_redirects=True)
    assert response.status_code == 200 # Not 201 because of redirect
    assert b"Login to Grasshopper Island" in response.data

def test_signup_post(client):
    """Test posting to login route."""
    response = client.post('/', data={'command': 'create'}, follow_redirects=True)
    assert response.status_code == 200 # Not 201 because of redirect
    assert b"Sign Up for Grasshopper Island" in response.data

def test_get_login(client):
    """Test the login route."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login to Grasshopper Island" in response.data

def test_get_signup(client):
    """Test the create an account route."""
    response = client.get('/signup')
    assert response.status_code == 200
    assert b"Sign Up for Grasshopper Island" in response.data

def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404