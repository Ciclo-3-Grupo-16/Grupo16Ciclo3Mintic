# Generated by Django 4.1.1 on 2022-09-15 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0011_rename_rol_usuario_identificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresos_gastos',
            name='nombre',
        ),
    ]
