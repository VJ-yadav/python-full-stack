import pytest
import uuid
import reflex as rx
from sqlmodel import Session, select

from python_full_stack.auth.state import MyRegisterState, SessionState
from python_full_stack.models import UserInfo
from reflex_local_auth.user import LocalUser

# Helper function to generate unique usernames for tests
def generate_unique_username():
    return f"testuser_{uuid.uuid4().hex[:8]}"

# Fixture to create a test database session
@pytest.fixture
def session():
    with rx.session() as session:
        yield session
        # Clean up test data after test
        session.rollback()

# Test registration validation
def test_registration_validation():
    state = MyRegisterState()
    
    # Test username validation
    result = state._validate_fields("ab", "password123", "password123", True)
    assert isinstance(result, rx.event.EventSpec)
    assert state.my_error_message == "Username must be at least 3 characters"
    
    # Test password validation
    result = state._validate_fields("validuser", "short", "short", True)
    assert isinstance(result, rx.event.EventSpec)
    assert state.my_error_message == "Password must be at least 8 characters"
    
    # Test password match validation
    result = state._validate_fields("validuser", "password123", "different", True)
    assert isinstance(result, rx.event.EventSpec)
    assert state.my_error_message == "Passwords do not match"
    
    # Test terms agreement validation
    result = state._validate_fields("validuser", "password123", "password123", False)
    assert isinstance(result, rx.event.EventSpec)
    assert state.my_error_message == "You must agree to the Terms of Service"
    
    # Test valid input
    result = state._validate_fields("validuser", "password123", "password123", True)
    assert result is None

# Test user registration
def test_user_registration(session):
    state = MyRegisterState()
    username = generate_unique_username()
    
    # Test registration with valid data
    form_data = {
        "username": username,
        "password": "password123",
        "confirm_password": "password123",
        "email": f"{username}@example.com",
        "terms_agreed": True
    }
    
    # Register user
    result = state.handle_registration(form_data)
    
    # Check if user was created
    user = session.query(LocalUser).filter(LocalUser.username == username).first()
    assert user is not None
    assert user.username == username
    
    # Test duplicate username
    state = MyRegisterState()
    result = state.handle_registration(form_data)
    assert isinstance(result, rx.event.EventSpec)
    assert f"Username '{username}' is already taken" in state.my_error_message

# Test email registration
def test_registration_with_email(session):
    state = MyRegisterState()
    username = generate_unique_username()
    email = f"{username}@example.com"
    
    # Test registration with valid data
    form_data = {
        "username": username,
        "password": "password123",
        "confirm_password": "password123",
        "email": email,
        "terms_agreed": True
    }
    
    # Register user with email
    result = state.handle_registration_email(form_data)
    
    # Check if user was created
    user = session.query(LocalUser).filter(LocalUser.username == username).first()
    assert user is not None
    
    # Check if UserInfo was created
    user_info = session.exec(select(UserInfo).where(UserInfo.user_id == user.id)).one_or_none()
    assert user_info is not None
    assert user_info.email == email

# Test login functionality
def test_login_functionality(session):
    # First create a test user
    state = MyRegisterState()
    username = generate_unique_username()
    password = "password123"
    
    form_data = {
        "username": username,
        "password": password,
        "confirm_password": password,
        "email": f"{username}@example.com",
        "terms_agreed": True
    }
    
    # Register user
    state.handle_registration_email(form_data)
    
    # Now test login
    login_state = SessionState()
    
    # Test with correct credentials
    login_state.do_login(username, password)
    assert login_state.is_authenticated
    assert login_state.authenticated_username == username
    
    # Test with incorrect password
    login_state = SessionState()
    login_state.do_login(username, "wrongpassword")
    assert not login_state.is_authenticated
    
    # Test with non-existent user
    login_state = SessionState()
    login_state.do_login("nonexistentuser", "password123")
    assert not login_state.is_authenticated