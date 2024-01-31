from django.urls import path

from . import views

app_name = "bitacora"

urlpatterns = [
    path("", views.index, name="index"),
    path("pais/list", views.pais_list, name="pais_list"),
    path("perfil/list", views.perfil_list, name="perfil_list"),
    path("perfil/create", views.perfil_create, name="perfil_create"),
    path("viaje/list", views.viaje_list, name="viaje_list"),
    path("viaje/create", views.viaje_create, name="viaje_create"),
]
