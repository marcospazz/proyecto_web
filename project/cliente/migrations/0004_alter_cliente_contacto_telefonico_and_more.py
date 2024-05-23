# Generated by Django 5.0.4 on 2024-05-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_cliente_contacto_telefonico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='contacto_telefonico',
            field=models.PositiveIntegerField(verbose_name='Teléfono movil'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nombre y Apellido'),
        ),
    ]
