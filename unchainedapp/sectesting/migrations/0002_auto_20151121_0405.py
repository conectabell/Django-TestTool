# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commexecuted',
            name='host',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='output',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='com_base',
            field=models.TextField(),
        ),
    ]
