# Generated by Django 4.1.1 on 2022-09-07 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0004_usuario_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
    ]