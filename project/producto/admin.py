from django.contrib import admin

from .models import *

admin.site.site_title = "Productos"


class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria_id", "nombre", "unidad_medida", "cantidad", "precio", "fecha_actualizacion")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria_id", "nombre")
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_actualizacion"


admin.site.register(ProductoCategoria, ProductoCategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
