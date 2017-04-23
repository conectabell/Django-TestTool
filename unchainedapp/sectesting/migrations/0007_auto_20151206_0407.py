# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0006_auto_20151205_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='info',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='presentacion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='resumen',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='resumen_ej',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='soluciones',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='vulns',
            field=models.TextField(null=True, blank=True),
        ),
    ]
