from django.urls import path

from . import views

app_name = "bitacora"

urlpatterns = [
    path("", views.index, name="index"),
    path("pais/list", views.pais_list, name="pais_list"),
    path("perfil/list", views.perfil_list, name="perfil_list"),
    path("perfil/create/<int:id>/", views.perfil_create, name="perfil_create"),
    path("viaje/list/<int:id>/", views.viaje_list, name="viaje_list"),
    path("viaje/create/<int:id>/", views.viaje_create, name="viaje_create"),
    path("perfil/borrar/<int:id>/", views.perfil_borrar, name="perfil_borrar"),
]
