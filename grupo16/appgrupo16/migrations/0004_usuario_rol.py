# Generated by Django 4.1.1 on 2022-09-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0003_rename_cargo_empleado_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
