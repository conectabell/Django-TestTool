# -*- coding: utf-8 -*-
#import subprocess
import os
import platform
from procfs import Proc
#from ..models import Test_Plano, CommExecuted, CommPredef


def getOSbasic():
    sysuname = os.uname()
    tsis = sysuname[0]
    ker = sysuname[2]
    mnom = sysuname[1]
    dev = {'tipo': tsis, 'kernel': ker, 'nombre': mnom}
    return dev


def getpybasic():
    pyv = platform.python_version()
    pyi = platform.python_implementation()
    pyc = platform.python_compiler()
    py = {'version': pyv, 'implementacion': pyi, 'compilador': pyc}
    return py


#Devuelve la info a la barra de estado
def getBarInfo():
    proc = Proc()
    fr = proc.meminfo.MemFree
    to = proc.meminfo.MemTotal
    ca = proc.meminfo.Cached
    frmb = fr / 1024
    tomb = to / 1024
    camb = ca / 1024
    avg = proc.loadavg
    mem = {'libre': frmb, 'total': tomb, 'cache': camb}
    bar = {'mem': mem, 'carga': avg}
    return bar


#Devuelve la carga del sistema y el contador de procesos
def getAvg():
    proc = Proc()
    load = proc.loadavg
    avg = load.average
    prs = load.entities
    average = {'avg': avg, 'prs': prs}
    return average


#Devuelve informacion de la memoria
def getMemoryInfo():
    proc = Proc()
    fr = proc.meminfo.MemFree
    to = proc.meminfo.MemTotal
    ca = proc.meminfo.Cached
    frmb = fr / 1024
    tomb = to / 1024
    camb = ca / 1024
    mem = {'libre': frmb, 'total': tomb, 'cache': camb}
    return mem


#Funcion que devuelve listados de procesos, dependiendo del string del primer
#parametro indicamos si queremos que devuelva la lista completa, o filtrando
#por procesos o por usuarios
def getProcessList(n="t", s=""):
    try:
        proc = Proc()
        if n == 't':
            procs = proc.processes
            proret = []
            for p in procs:
                c = str(p).split(":")
                a = c[0].replace("<Process", "")
                b = c[1].replace(">", "")
                dic = {'pid': a, 'nombre': b}
                proret.append(dic)
            return proret
        elif n == 'g':
            try:
                proc = Proc()
                pyt = proc.processes.cmdline(s)
                return pyt
            except Exception, e:
                ret = "No se encuentra el nombre"
                retu = {'nombre': ret, 'error': e}
                return retu
        elif n == 'u':
            try:
                proc = Proc()
                pyt = proc.processes.user(s)
                return pyt
            except Exception, e:
                ret = "No se encuentra el usuario"
                retu = {'nombre': ret, 'error': e}
                return retu
        else:
            raise ValueError('Valor del PARAMETRO INCORRECTO o nulo')
    except Exception, e:
        return e


#Estas funciones no son necesarias, las dejo aqui como ejemplo
def getProcessListGrep(n):
    try:
        proc = Proc()
        pyt = proc.processes.cmdline(n)
        return pyt
    except Exception, e:
        ret = "No se encuentra el nombre"
        retu = {'nombre': ret, 'error': e}
        return retu


def getProcessListUser(u):
    try:
        proc = Proc()
        pyt = proc.processes.user(u)
        return pyt
    except Exception, e:
        ret = "No se encuentra el usuario"
        retu = {'nombre': ret, 'error': e}
        return retu