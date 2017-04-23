# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0005_commpredef_vista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ruta_sistema',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='comando_base',
            field=models.ForeignKey(blank=True, to='sectesting.CommPredef', null=True),
        ),
    ]
