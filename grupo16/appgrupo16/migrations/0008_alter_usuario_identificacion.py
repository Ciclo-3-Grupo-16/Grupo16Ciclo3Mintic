# Generated by Django 4.1.1 on 2022-09-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgrupo16', '0007_alter_usuario_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='identificacion',
            field=models.CharField(max_length=50),
        ),
    ]
