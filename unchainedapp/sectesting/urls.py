# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.principal, name='index'),
    url(r'^principal$', views.principal),
    url(r'^clientes/list', views.clientes_list),
    url(r'^clientes/detail/(?P<pk>[0-9]+)/$', views.cliente_detail),
    url(r'^comandos/list', views.command_list),
    url(r'^test/list', views.test_list),
    #url(r'^test/ping1$', views.ping1_test),
    #url(r'^test/whois$', views.whois_test),
    url(r'^test/launch/(?P<pk>[0-9]+)/(?P<nom>.*)/$', views.lanz_com_predef),
    #url(r'^test/nmap_fast$', views.nmap_fast),
    #url(r'^test/nmap_a$', views.nmap_a),
    #url(r'^test/nmap_all_tcp$', views.nmap_all_tcp),
    url(r'^test/detail/(?P<pk>[0-9]+)/$', views.test_detail),
    url(r'^test/detail/command-detail/(?P<pk>[0-9]+)/$', views.command_detail),
    url(r'^informes/list', views.informe_list),
    url(r'^informes/escribir', views.escribir_informe),
    url(r'^informes/detail/(?P<pk>[0-9]+)/$', views.informe_detail),
    url(r'^principal/systeminfo$', views.systemInfo),
]