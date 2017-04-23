# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0003_auto_20151122_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commexecuted',
            name='output',
            field=models.TextField(null=True, blank=True),
        ),
    ]
