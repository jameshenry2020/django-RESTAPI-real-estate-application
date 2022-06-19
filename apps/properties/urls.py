from django.urls import path

from .views import (PropertyCreateApiView,
                    PropertyListView, PropertyDetailView, 
                    PropertyDeleteApiView, AgentPropertyListView,
                    PropertyUpdateView, UploadPropertyImages
                    )

urlpatterns = [
    path("properties-list/", PropertyListView.as_view(), name="properties-list"),
    path(
        "agent-properties/<uuid:agent_id>/",
        AgentPropertyListView.as_view(),
        name="listing",
    ),
    path(
        "property-detail/<slug:slug>/",
        PropertyDetailView.as_view(),
        name="propery-detail",
    ),
    path(
        "property-update/<slug:slug>/update/",
        PropertyUpdateView.as_view(),
        name="property-update",
    ),
    path("property-create/", PropertyCreateApiView.as_view(), name="property-create"),
    path(
        "upload-property-image/", UploadPropertyImages.as_view(), name="property-image"
    ),
    path(
        "property-delete/<slug:slug>/",
        PropertyDeleteApiView.as_view(),
        name="delete-property",
    ),
]
