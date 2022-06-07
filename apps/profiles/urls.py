from django.urls import path
from .views import GetUserProfile, UpdateUserProfile



urlpatterns = [
    path("me/", GetUserProfile.as_view(), name='get_profile'),
    path("update/<uuid:user_id>/", UpdateUserProfile.as_view(), name='profile_update'),
]