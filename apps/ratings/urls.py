from django.urls import path

from .views import create_agent_review

urlpatterns = [
    path("agent/<uuid:agent_id>/", create_agent_review, name="review"),
]
