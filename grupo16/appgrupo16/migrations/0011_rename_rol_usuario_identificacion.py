# Generated by Django 4.1.1 on 2022-09-08 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0010_rename_identificacion_usuario_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='rol',
            new_name='identificacion',
        ),
    ]