# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectesting', '0002_auto_20151121_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_plano',
            name='software',
        ),
        migrations.RemoveField(
            model_name='test_plano',
            name='test',
        ),
        migrations.AddField(
            model_name='commexecuted',
            name='test',
            field=models.ForeignKey(default='1', to='sectesting.Test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_plano',
            name='salidaerr_comando',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observaciones',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='web1',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra0',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra1',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra2',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra3',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra4',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra5',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commexecuted',
            name='extra6',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra0',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra1',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra2',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra3',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra4',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra5',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_extra6',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_host',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='commpredef',
            name='mod_output',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='soft',
            name='comentarios',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='soft',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='observaciones',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='ruta',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test_plano',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test_plano',
            name='observaciones',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test_plano',
            name='salida_comando',
            field=models.TextField(null=True, blank=True),
        ),
    ]
