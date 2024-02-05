from django.urls import path

from . import views

app_name = "bitacora"

urlpatterns = [
    path("", views.index, name="index"),
    path("pais/list", views.pais_list, name="pais_list"),
    path("perfil/list", views.perfil_list, name="perfil_list"),
    path("perfil/create/<int:id>/", views.perfil_create, name="perfil_create"),
    path("perfil/borrar/<int:id>/", views.perfil_borrar, name="perfil_borrar"),
    path("perfil/viaje_list/<int:id>/", views.perfil_viaje_list, name="perfil_viaje_list"),
    path("viaje/list/<int:id>/", views.viaje_list, name="viaje_list"),
    path("viaje/create/<int:id>/", views.viaje_create, name="viaje_create"),
    path("viaje/editar/<int:id>/", views.viaje_editar, name="viaje_editar"),
    path("viaje/borrar/<int:id>/", views.viaje_borrar, name="viaje_borrar"),
    path("viaje/etapa_list/<int:id>/", views.viaje_etapa_list, name="viaje_etapa_list"),
    path("viaje/etapa_create/<int:id>/", views.viaje_etapa_create, name="viaje_etapa_create"),
    path("viaje/etapa_editar/<int:id>/", views.viaje_etapa_editar, name="viaje_etapa_editar"),
    path("viaje/etapa_borrar/<int:id>/", views.viaje_etapa_borrar, name="viaje_etapa_borrar"),
]
