# Generated by Django 4.1.1 on 2022-09-05 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='identificacion',
            new_name='nombre_usuario',
        ),
    ]
