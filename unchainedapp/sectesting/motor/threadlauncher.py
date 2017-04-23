# -*- coding: utf-8 -*-
#!/usr/bin/python
#from django.db import models
import threading
from datetime import datetime
#import time
#from django.utils import timezone
import subprocess
from ..models import Test_Plano, CommExecuted, CommPredef


class CommandThreadBH (threading.Thread):
    def __init__(self, threadID, name, com, hos, p):
        threading.Thread.__init__(self)
        aid = threading.active_count()
        aid += 1
        #self.threadID = threadID
        self.name = name
        self.comando = CommPredef.objects.get(pk=com)
        self.host = hos
        self.pkh = CommExecuted.objects.get(pk=p)

    def run(self):
        cmbase = self.comando.com_base
        host = self.host
        pkh = self.pkh
        pkh.hora_exec = unicode(datetime.now())
        pkh.estado = "init"
        pkh.save()
        comando = cmbase + " " + host
        nuevoplano = Test_Plano.objects.create(titulo=self.name, comando=pkh)
        nuevoplano.save()
        try:
            proc = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            pkh.hora_fin = datetime.now()
            pkh.estado = "ended"
            pkh.save()
            print "NUEVOPLANO"
            print nuevoplano
            nuevoplano.titulo=self.name
            nuevoplano.salida_comando=out
            nuevoplano.salidaerr_comando=err
            nuevoplano.comando=pkh
            nuevoplano.save()
        except Exception as e:
            print e
            nuevoplano.salidaerr_comando=str(e)
            nuevoplano.save()
            pkh.estado = "error"
            pkh.save()
