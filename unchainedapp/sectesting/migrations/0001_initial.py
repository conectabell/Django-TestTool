# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
                ('nif', models.CharField(max_length=50)),
                ('fecha_alta', models.DateTimeField(default=django.utils.timezone.now)),
                ('web1', models.TextField(null=True)),
                ('observaciones', models.TextField(null=True)),
                ('ruta_sistema', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommExecuted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.TextField(null=True)),
                ('output', models.TextField(null=True)),
                ('extra0', models.TextField(null=True)),
                ('extra1', models.TextField(null=True)),
                ('extra2', models.TextField(null=True)),
                ('extra3', models.TextField(null=True)),
                ('extra4', models.TextField(null=True)),
                ('extra5', models.TextField(null=True)),
                ('extra6', models.TextField(null=True)),
                ('hora_exec', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_fin', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado', models.CharField(default=b'noinit', max_length=10, choices=[(b'noinit', b'No Iniciado'), (b'init', b'Ejecutando'), (b'ended', b'Terminado')])),
            ],
        ),
        migrations.CreateModel(
            name='CommPredef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
                ('com_base', models.TextField(null=True)),
                ('mod_host', models.TextField(null=True)),
                ('mod_output', models.TextField(null=True)),
                ('mod_extra0', models.TextField(null=True)),
                ('mod_extra1', models.TextField(null=True)),
                ('mod_extra2', models.TextField(null=True)),
                ('mod_extra3', models.TextField(null=True)),
                ('mod_extra4', models.TextField(null=True)),
                ('mod_extra5', models.TextField(null=True)),
                ('mod_extra6', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.TextField()),
                ('presentacion', models.TextField()),
                ('resumen_ej', models.TextField()),
                ('resumen', models.TextField()),
                ('info', models.TextField()),
                ('vulns', models.TextField()),
                ('soluciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
                ('comentarios', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_alta', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo', models.CharField(max_length=30, choices=[(b'web', b'Web'), (b'servicios', b'Servicios'), (b'basico', b'Basico')])),
                ('observaciones', models.TextField(null=True)),
                ('ruta', models.TextField(null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cliente', models.ForeignKey(to='sectesting.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Plano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
                ('salida_comando', models.TextField(null=True)),
                ('observaciones', models.TextField(null=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('comando', models.ForeignKey(to='sectesting.CommExecuted')),
                ('software', models.ForeignKey(to='sectesting.Soft')),
                ('test', models.ForeignKey(to='sectesting.Test')),
            ],
        ),
        migrations.AddField(
            model_name='informe',
            name='test',
            field=models.ForeignKey(to='sectesting.Test'),
        ),
        migrations.AddField(
            model_name='commpredef',
            name='software',
            field=models.ForeignKey(to='sectesting.Soft'),
        ),
        migrations.AddField(
            model_name='commexecuted',
            name='comando_base',
            field=models.ForeignKey(to='sectesting.CommPredef'),
        ),
    ]
