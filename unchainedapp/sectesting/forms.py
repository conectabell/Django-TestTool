# -*- coding: utf-8 -*-
from django import forms
from .models import CommExecuted, Informe


class Ping1Form(forms.ModelForm):

    class Meta:
        model = CommExecuted
        fields = ('test', 'host')


class Whois1Form(forms.ModelForm):

    class Meta:
        model = CommExecuted
        fields = ('test', 'host')


class NmapAForm(forms.ModelForm):

    class Meta:
        model = CommExecuted
        fields = ('test', 'host')


class NmapAllTCPForm(forms.ModelForm):

    class Meta:
        model = CommExecuted
        fields = ('test', 'host')


class InformeForm(forms.ModelForm):

    class Meta:
        model = Informe
        fields = ('titulo', 'presentacion', 'resumen_ej', 'resumen', 'info',
                                                'vulns', 'soluciones', 'test')