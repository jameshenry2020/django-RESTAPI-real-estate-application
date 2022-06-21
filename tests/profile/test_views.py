import pytest
from apps.profiles.models import Profile, HostAgent
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from apps.users.models import User
from django.contrib.auth.tokens import default_token_generator
from djoser.utils import encode_uid


client=APIClient()
@pytest.mark.django_db
def test_user_register_endpoint(user_factory):
    payload={
        'first_name':'john',
        'last_name':'peter',
        'phone':'+2349057484336',
        'email':'testuser1@gmail.com',
        'password':'test4321',
        're_password':'test4321'
    }
    res =client.post('/api/v1/auth/users/', payload)
    assert res.status_code == 201


#testing with superuser bcos superuser account are activated by default while normal user need to activate account first
 

def test_user_cannot_become_agent_without_authentication(profile):
    endpoint = '/api/v1/profile/create-agent/'
    user_profile=profile
    agent_data = {'brand_name':'first real estate agency','license':'2387f9', 'office_address':'24 allen avenue', 'profile':user_profile}   
    response = client.post(endpoint, agent_data)
    assert response.status_code == 401
