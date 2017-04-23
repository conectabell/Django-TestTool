from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
#from django.core.validators import validate_ipv4_address


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    nif = models.CharField(max_length=50)
    fecha_alta = models.DateTimeField(default=timezone.now)
    web1 = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    ruta_sistema = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.empresa


class Test(models.Model):
    WEB = "web"
    SERV = "servicios"
    BAS = "basico"
    TIPOS_TEST = (
        (WEB, 'Web'),
        (SERV, 'Servicios'),
        (BAS, 'Basico'),
        )
    author = models.ForeignKey('auth.User')
    cliente = models.ForeignKey('Cliente')
    fecha_alta = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=30, choices=TIPOS_TEST)
    observaciones = models.TextField(null=True, blank=True)
    ruta = models.TextField(null=True, blank=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        devolver = self.cliente.empresa + " -- " + unicode(self.fecha_alta)
        return devolver


class Soft(models.Model):
    nombre = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        devuelve = self.nombre + " (" + self.version + ")"
        return devuelve


class CommPredef(models.Model):
    software = models.ForeignKey('Soft')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    com_base = models.TextField()
    mod_host = models.TextField(null=True, blank=True)
    mod_output = models.TextField(null=True, blank=True)
    mod_extra0 = models.TextField(null=True, blank=True)
    mod_extra1 = models.TextField(null=True, blank=True)
    mod_extra2 = models.TextField(null=True, blank=True)
    mod_extra3 = models.TextField(null=True, blank=True)
    mod_extra4 = models.TextField(null=True, blank=True)
    mod_extra5 = models.TextField(null=True, blank=True)
    mod_extra6 = models.TextField(null=True, blank=True)
    vista = models.TextField(null=True, blank=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class CommExecuted(models.Model):
    NOINIT = "noinit"
    INIT = "init"
    ENDED = "ended"
    ERROR = "error"
    ESTADOS = (
        (NOINIT, 'No Iniciado'),
        (INIT, 'Ejecutando'),
        (ENDED, 'Terminado'),
        (ERROR, 'Error'),
        )
    comando_base = models.ForeignKey('CommPredef',
        null=True,
        blank=True)

    host = models.TextField(
        validators=[
            RegexValidator(
                #Expresion regular partida en trozos, valida nombre de dominio
                #o direccion IP, una u otra pueden ser validas
                regex="(^([a-zA-Z0-9](?:(?:[a-zA-Z0-9-]*|(?<!-)\.(?![-.]))" +
                "*[a-zA-Z0-9]+)?)$" +
                ")|(" +
                "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4]" +
                "[0-9]|[01]?[0-9][0-9]?)){3})",
                message="El host introducido NO ES VALIDO, escriba un nombre " +
                "de host o una direccion IP",),
                ]
        )
    output = models.TextField(null=True, blank=True)
    extra0 = models.TextField(null=True, blank=True)
    extra1 = models.TextField(null=True, blank=True)
    extra2 = models.TextField(null=True, blank=True)
    extra3 = models.TextField(null=True, blank=True)
    extra4 = models.TextField(null=True, blank=True)
    extra5 = models.TextField(null=True, blank=True)
    extra6 = models.TextField(null=True, blank=True)
    hora_exec = models.DateTimeField(default=timezone.now)
    hora_fin = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=NOINIT)
    test = models.ForeignKey('Test')

    def publish(self):
        self.save()

    def __str__(self):
        devuelve = (unicode(self.hora_exec) + " Soft: "
        + self.comando_base.software.nombre + " Host: " + self.host)
        return devuelve


class Test_Plano(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    comando = models.ForeignKey('CommExecuted')
    salida_comando = models.TextField(null=True, blank=True)
    salidaerr_comando = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        devolver = (self.titulo + " / CLI: " + self.comando.host +
                                        "/ FECHA: " + str(self.fecha))
        return devolver


class Informe(models.Model):

    titulo = models.TextField()
    presentacion = models.TextField(null=True, blank=True)
    resumen_ej = models.TextField(null=True, blank=True)
    resumen = models.TextField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    vulns = models.TextField(null=True, blank=True)
    soluciones = models.TextField(null=True, blank=True)
    test = models.ForeignKey('Test')
    fecha = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        devolver = (self.titulo + " / CLI: " + self.test.cliente.empresa +
                                        "/ FECHA: " + str(self.fecha))
        return devolver