from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    """Categoría de productos"""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")

    def __str__(self) -> str:
        """Representa la instancia de la clase como una cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "categoría de producto"
        verbose_name_plural = "categorías de productos"


class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100)
    cantidad = models.FloatField()
    precio = models.FloatField()
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(
        null=True, blank=True, default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
