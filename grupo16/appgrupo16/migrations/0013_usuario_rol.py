# Generated by Django 4.1.1 on 2022-09-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0012_remove_ingresos_gastos_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
