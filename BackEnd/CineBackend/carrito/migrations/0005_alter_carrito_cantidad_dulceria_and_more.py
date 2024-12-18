# Generated by Django 5.1.4 on 2024-12-18 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_remove_carrito_productos_dulceria_and_more'),
        ('usuarios', '0002_usuario_es_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='cantidad_dulceria',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='cantidad_pelicula',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
    ]