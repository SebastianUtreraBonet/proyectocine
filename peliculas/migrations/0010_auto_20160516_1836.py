# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0009_auto_20160516_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actores',
            name='foto',
            field=models.ImageField(upload_to='static/img/actores'),
        ),
        migrations.AlterField(
            model_name='directores',
            name='foto',
            field=models.ImageField(upload_to='static/img/directores'),
        ),
        migrations.AlterField(
            model_name='paises',
            name='bandera',
            field=models.ImageField(upload_to='static/img/banderas'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='caratula',
            field=models.ImageField(upload_to='static/img/caratulas'),
        ),
        migrations.AlterField(
            model_name='productoras',
            name='imagen',
            field=models.ImageField(upload_to='static/img/productoras'),
        ),
    ]
