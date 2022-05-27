
from django.contrib import admin
from django.urls import path
from django.conf import settings, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)