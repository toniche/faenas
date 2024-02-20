# Generated by Django 3.0.1 on 2020-03-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BonoRepara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=200)),
                ('Cliente', models.CharField(max_length=200)),
                ('FechaBono', models.DateField(verbose_name='Fecha de Creación')),
                ('Expira', models.DateField(verbose_name='Fecha Caducidad')),
            ],
            options={
                'verbose_name': 'Bonos',
                'verbose_name_plural': 'Bonos',
                'ordering': ['Cliente'],
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Cif', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('Localidad', models.CharField(max_length=200)),
                ('Provincia', models.CharField(max_length=200)),
                ('CP', models.IntegerField()),
                ('Alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('Otros', models.TextField(max_length=600, verbose_name='Otros')),
            ],
            options={
                'verbose_name': 'Clientes',
                'verbose_name_plural': 'Clientes',
                'ordering': ['Nombre'],
            },
        ),
        migrations.CreateModel(
            name='Reparaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente', models.CharField(max_length=40)),
                ('Fecha', models.DateTimeField(verbose_name='Fecha de creación')),
                ('Motivo', models.CharField(max_length=200)),
                ('Estado', models.BooleanField()),
                ('Descripcion', models.TextField(max_length=600, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Reparaciones',
                'verbose_name_plural': 'Reparaciones',
                'ordering': ['Cliente'],
            },
        ),
    ]
