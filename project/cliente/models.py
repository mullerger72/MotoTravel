from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
