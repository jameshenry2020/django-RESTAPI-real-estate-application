import pytest



def test_user_str(base_user):
    """Test the custom user model string representation"""
    assert base_user.__str__() == f"{base_user.email}"


def test_user_full_name(base_user):
    """Test that the user models get_full_name method works"""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name

def test_base_user_email_is_normalized(base_user):
    """Test that a new users email is normalized"""
    email = "henry@REALESTATE.COM"
    assert base_user.email == email.lower()

def test_user_email_incorrect(user_factory):
    """Test that an Error is raised when a non valid email is provided"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="realestate.com")
    assert str(err.value) == "you must provide a valid email address"

def test_create_user_with_no_email(user_factory):
    """Test that creating a new user with no email address raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"

def test_create_user_with_no_firstname(user_factory):
    """Test creating a new user without a firstname raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "First name is required"


def test_create_user_with_no_lastname(user_factory):
    """Test creating a new user without a lastname raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Last name is required"

def test_create_user_with_no_phone(user_factory):
    """Test creating a new user without a lastname raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(phone=None)
    assert str(err.value) == "phone number is required"

def test_create_user_with_no_is_superuser(user_factory):
    """Test creating a superuser without a password raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "is superuser must be true for admin user"

def test_create_superuser_with_no_is_staff(user_factory):
    """Test creating a superuser without a password raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "is staff must be true for admin user"