from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"


class Perfil(models.Model):
    user = models.ForeignKey(
       User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="User"
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    moto = models.CharField(max_length=100)
    lugar_residencia = models.CharField(max_length=100)
    pais_origen_id = models.ForeignKey(
        Pais, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="País de origen"
    )

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre} - {self.moto} - {self.lugar_residencia}"

class Viaje(models.Model):
    perfil = models.ForeignKey(
        Perfil, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Usuario"
        )
    fecha_ini = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    localidad_ini = models.CharField(max_length=100, verbose_name="Localidad de Inicio ")
    localidad_fin = models.CharField(max_length=100, verbose_name="Localidad Destino   ")
    km_recorridos = models.FloatField()
    comentarios = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.fecha_ini} - {self.fecha_fin} - {self.localidad_ini} - {self.localidad_fin} - {self.km_recorridos} - {self.comentarios}"

class Viaje_Etapa(models.Model):
    viaje = models.ForeignKey(
        Viaje, null=True, blank=True, on_delete=models.SET_NULL
        )
    sentido = models.CharField(
        max_length=50, blank=True,
        choices= [             
            ('Ida', 'Ida'), 
            ('Vuelta', 'Vuelta'), 
        ], 
        verbose_name="Sentido de la Etapa "
        )
    fecha_ini = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    localidad_ini = models.CharField(max_length=100, verbose_name="Localidad de Inicio ")
    localidad_fin = models.CharField(max_length=100, verbose_name="Localidad de Fin   ")
    km_recorridos = models.FloatField()
    comentarios = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.fecha_ini} - {self.fecha_fin} - {self.localidad_ini} - {self.localidad_fin} - {self.km_recorridos} - {self.comentarios}"
