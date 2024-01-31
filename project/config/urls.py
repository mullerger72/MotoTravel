from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("bitacora", include("bitacora.urls")),
#    path("clientes/", include("cliente.urls")),
#    path("productos/", include("producto.urls")),
]
