# Generated by Django 5.1.4 on 2024-12-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('REGULAR', 'Regular')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=255)),
                ('function_types', models.ManyToManyField(help_text='Select function types available in this theater', to='cines.functiontype')),
            ],
        ),
    ]
