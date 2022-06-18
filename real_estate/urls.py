from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include("djoser.urls")),
    path('api/v1/auth/', include("djoser.urls.jwt")),
    path('api/v1/profile/', include('apps.profiles.urls')),
    path('api/v1/property/', include('apps.properties.urls')),
    path('api/v1/rating/', include('apps.ratings.urls')),
    path('api/v1/enquiry/', include('apps.enquiries.urls'))
]
