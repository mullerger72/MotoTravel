# Generated by Django 5.0.1 on 2024-02-06 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0008_alter_viaje_localidad_fin_alter_viaje_localidad_ini_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje_etapa',
            name='viaje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bitacora.viaje'),
        ),
    ]
