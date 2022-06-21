import pytest




def test_profile_str(profile):
    """Test the profile model string representation"""
    assert profile.__str__() == f"{profile.user.first_name} profile"



@pytest.mark.django_db
def test_host_agent_str(host_factory):
    agent = host_factory.create()
    assert agent.__str__() == f"{agent.brand_name}"


