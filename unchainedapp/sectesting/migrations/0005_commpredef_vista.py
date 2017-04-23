# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0004_auto_20151122_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='commpredef',
            name='vista',
            field=models.TextField(null=True, blank=True),
        ),
    ]
