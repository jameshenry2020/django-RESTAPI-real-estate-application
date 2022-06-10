from django.urls import path
from .views import (GetUserProfile, 
                    UpdateUserProfile,
                   BecomeAnAgent, 
                   AgentListView,
                   GetAgentProfileDetail,)



urlpatterns = [
    path("me/", GetUserProfile.as_view(), name='get_profile'),
    path("create-agent/", BecomeAnAgent.as_view(), name='become-an-agent'),
    path('agent-list/', AgentListView.as_view(), name='agent-list'),
    path('agent/<str:business_name>/', GetAgentProfileDetail.as_view()),
    path("update/<uuid:user_id>/", UpdateUserProfile.as_view(), name='profile_update'),
]