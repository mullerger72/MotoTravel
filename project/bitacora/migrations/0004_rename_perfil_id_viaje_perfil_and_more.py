# Generated by Django 5.0.1 on 2024-01-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0003_viaje_perfil_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viaje',
            old_name='perfil_id',
            new_name='perfil',
        ),
        migrations.AlterField(
            model_name='viaje',
            name='localidad_ini',
            field=models.CharField(max_length=100, verbose_name='Localidad de Inicio'),
        ),
    ]