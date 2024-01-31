from django.contrib import admin

from .models import Viaje, Perfil, Pais

admin.site.register(Pais)
admin.site.register(Viaje)
admin.site.register(Perfil)
