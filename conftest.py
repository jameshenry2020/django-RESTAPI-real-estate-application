import email
import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import ProfileFactory, UserFactory, HostFactory

register(ProfileFactory)
register(UserFactory)
register(HostFactory)


client=APIClient()

@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


   
    

@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user

@pytest.fixture
def profile(db, profile_factory, base_user):
    user_profile = profile_factory.create(user=base_user)
    return user_profile