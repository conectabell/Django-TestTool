# -*- coding: utf-8 -*-
import subprocess
from datetime import datetime
from ..models import Test_Plano, CommExecuted
#class commandlauncher():
#
 #   def __init__(self):
  #      super(commandlauncher, self).__init__()
   # #lint:enable


def LaunchPing(h, p):
    host = h
    pkh = CommExecuted.objects.get(pk=p)
    comando = "ping -c5 " + host
    proc = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    pkh.hora_fin = unicode(datetime.now())
    pkh.estado = "ended"
    pkh.save()
    nuevoplano = Test_Plano.objects.create(titulo="Ping",
                                        salida_comando=out,
                                        salidaerr_comando=err, comando=pkh)
    nuevoplano.save()


def LaunchWhois(h, p):
    host = h
    pkh = CommExecuted.objects.get(pk=p)
    cmbase = pkh.comando_base.com_base
    comando = cmbase + " " + host
    proc = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    pkh.hora_fin = unicode(datetime.now())
    pkh.estado = "ended"
    pkh.save()
    nuevoplano = Test_Plano.objects.create(titulo="Whois", salida_comando=out,
                                            salidaerr_comando=err, comando=pkh)
    nuevoplano.save()
