from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("root_bitacora/", admin.site.urls),
    path("", include("core.urls")),
    path("bitacora", include("bitacora.urls")),
]
