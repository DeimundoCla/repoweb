# Generated by Django 4.0.4 on 2022-06-02 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotizacion', models.FloatField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('variacion', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Dolar_blue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotizacion', models.FloatField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('variacion', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Euro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotizacion', models.FloatField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('variacion', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Reais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotizacion', models.FloatField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('variacion', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
    ]
