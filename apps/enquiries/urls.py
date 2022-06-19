from django.urls import path

from .views import send_enquiry_message

urlpatterns = [
    path("message/<uuid:property_id>/", send_enquiry_message, name="enquiry-message"),
]
