# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0007_auto_20151206_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
