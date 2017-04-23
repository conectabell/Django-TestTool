from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from .models import Test, Cliente, CommExecuted, Test_Plano, CommPredef, Informe
from .forms import Whois1Form
#from .forms import NmapAForm, NmapAllTCPForm
from .forms import InformeForm
from .motor.commandlauncher import *
from .motor.infosystem import *
from .motor.threadlauncher import CommandThreadBH
from django.contrib.auth.decorators import login_required


def principal(request):
    ob = getOSbasic()
    pb = getpybasic()
    mem = getMemoryInfo
    return render(request, 'sectesting/principal.html', {'syst': ob,
                                                        'pyt': pb,
                                                        'mem': mem})


@login_required(login_url='django.contrib.auth.views.login')
def test_list(request):
    tests = Test.objects.all()
    return render(request, 'sectesting/test_list.html', {'tests': tests})


@login_required(login_url='django.contrib.auth.views.login')
def test_detail(request, pk):
    #thtest = Test.objects.get(pk=pk)
    cmds = CommExecuted.objects.filter(test=pk)
    tst = get_object_or_404(Test, pk=pk)
    return render(request, 'sectesting/test_detail.html',
                            {'tst': tst, 'cmds': cmds})


@login_required(login_url='django.contrib.auth.views.login')
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'sectesting/cliente_list.html',
                                    {'clientes': clientes})


@login_required(login_url='django.contrib.auth.views.login')
def cliente_detail(request, pk):
    cln = get_object_or_404(Cliente, pk=pk)
    return render(request, 'sectesting/cliente_detail.html', {'cln': cln})


@login_required(login_url='django.contrib.auth.views.login')
def command_list(request):
    cmdos = CommPredef.objects.all()
    return render(request, 'sectesting/command_list.html',
                                    {'comandos': cmdos})


@login_required(login_url='django.contrib.auth.views.login')
def command_detail(request, pk):
    tplain = get_object_or_404(Test_Plano, comando=pk)
    cmd = CommExecuted.objects.get(pk=pk)
    return render(request, 'sectesting/command_detail.html',
                         {'cmd': cmd, 'tplain': tplain})


@login_required(login_url='django.contrib.auth.views.login')
def informe_list(request):
    informes = Informe.objects.all()
    return render(request, 'sectesting/informe_list.html',
                                    {'informes': informes})


@login_required(login_url='django.contrib.auth.views.login')
def informe_detail(request, pk):
    informe = get_object_or_404(Informe, pk=pk)
    return render(request, 'sectesting/informe_detail.html',
                                    {'informe': informe})


@login_required(login_url='django.contrib.auth.views.login')
def escribir_informe(request):
    if request.method == "POST":
        form = InformeForm(request.POST)
        if form.is_valid():
            inf = form.save(commit=False)
            inf.save()
            return informe_list(request)
    else:
        form = InformeForm()
    return render(request, 'sectesting/escribir_informe.html', {'form': form})


#@login_required(login_url='django.contrib.auth.views.login')
#def ping1_test(request):
    ##compredef = CommPredef.objects.get(pk=)
    #if request.method == "POST":
        #form = Ping1Form(request.POST)
        #if form.is_valid():
            #com = form.save(commit=False)
            #host = com.host
            #base = 1
            #com.save()
            #pkh = com.pk
            #compredef = CommPredef.objects.get(pk=base)
            #comlaunched = CommExecuted.objects.get(pk=pkh)
            #comlaunched.comando_base = compredef
            #comlaunched.save()
            #LaunchPing(host, pkh)
            #return test_list(request)
    #else:
        #form = Ping1Form()
    #return render(request, 'sectesting/ping1.html', {'form': form})


#@login_required(login_url='django.contrib.auth.views.login')
#def whois_test(request):
    ##compredef = CommPredef.objects.get(pk=)
    #if request.method == "POST":
        #form = Whois1Form(request.POST)
        #if form.is_valid():
            #com = form.save(commit=False)
            #host = com.host
            #base = 2
            #com.save()
            #pkh = com.pk
            #compredef = CommPredef.objects.get(pk=base)
            #comlaunched = CommExecuted.objects.get(pk=pkh)
            #comlaunched.comando_base = compredef
            #comlaunched.save()
            #LaunchWhois(host, pkh)
            #return test_list(request)
    #else:
        #form = Whois1Form()
    #return render(request, 'sectesting/whois.html', {'form': form})


#@login_required(login_url='django.contrib.auth.views.login')
#def nmap_fast(request):
    #if request.method == "POST":
        #form = Whois1Form(request.POST)
        #if form.is_valid():
            #com = form.save(commit=False)
            #host = com.host
            #base = 3
            #com.save()
            #compredef = CommPredef.objects.get(pk=base)
            #pkh = com.pk
            #comlaunched = CommExecuted.objects.get(pk=pkh)
            #comlaunched.comando_base = compredef
            #comlaunched.save()
            #thread1 = CommandThreadBH(1, "NmapFast", base, host, pkh)
            #thread1.start()
            #return test_list(request)
    #else:
        #form = NmapFastForm()
    #return render(request, 'sectesting/nmap_fast.html', {'form': form})


#@login_required(login_url='django.contrib.auth.views.login')
#def nmap_a(request):
    #if request.method == "POST":
        #form = Whois1Form(request.POST)
        #if form.is_valid():
            #com = form.save(commit=False)
            #host = com.host
            #base = 4
            #com.save()
            #compredef = CommPredef.objects.get(pk=base)
            #pkh = com.pk
            #comlaunched = CommExecuted.objects.get(pk=pkh)
            #comlaunched.comando_base = compredef
            #comlaunched.save()
            #thread1 = CommandThreadBH(2, "Nmap -A", base, host, pkh)
            #thread1.start()
            #return test_list(request)
    #else:
        #form = NmapAForm()
    #return render(request, 'sectesting/nmap_a.html', {'form': form})


#@login_required(login_url='django.contrib.auth.views.login')
#def nmap_all_tcp(request):
    #if request.method == "POST":
        #form = NmapAllTCPForm(request.POST)
        #if form.is_valid():
            #com = form.save(commit=False)
            #host = com.host
            #base = 5
            #com.save()
            #compredef = CommPredef.objects.get(pk=base)
            #pkh = com.pk
            #comlaunched = CommExecuted.objects.get(pk=pkh)
            #comlaunched.comando_base = compredef
            #comlaunched.save()
            #thread1 = CommandThreadBH(3, "Nmap All TCP", base, host, pkh)
            #thread1.start()
            #return test_list(request)
    #else:
        #form = NmapAllTCPForm()
    #return render(request, 'sectesting/nmap_fullrange.html', {'form': form})


@login_required(login_url='django.contrib.auth.views.login')
def lanz_com_predef(request, pk, nom):
    if request.method == "POST":
        form = Whois1Form(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            host = com.host
            base = pk
            nombre = nom
            com.save()
            compredef = CommPredef.objects.get(pk=base)
            pkh = com.pk
            comlaunched = CommExecuted.objects.get(pk=pkh)
            comlaunched.comando_base = compredef
            comlaunched.save()
            thread1 = CommandThreadBH(2, nombre, base, host, pkh)
            thread1.start()
            return test_list(request)
    else:
        form = Whois1Form()
        nom = nom
    return render(request, 'sectesting/whois.html', {'form': form, 'nom': nom})


def systemInfo(request):
    ob = getOSbasic()
    pb = getpybasic()
    mem = getMemoryInfo
    pro = getProcessList
    return render(request, 'sectesting/system_info.html', {'syst': ob,
                                                        'pyt': pb,
                                                        'mem': mem,
                                                        'pro': pro})