# Generated by Django 3.0.1 on 2024-02-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faenas', '0003_auto_20200327_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparaciones',
            name='Email',
            field=models.EmailField(default=0, max_length=254, verbose_name='Correo Electrónico'),
            preserve_default=False,
        ),
    ]
