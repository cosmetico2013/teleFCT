from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empresa (models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nombre)


class Sede (models.CharField):
    Empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    #cpsed = models.CharField(max_length=100)


class Contacto (models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return (str(self.nombre)+" "+str(self.apellidos))


class Contrato (models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #pra = models.DecimalField(max_digits=10,decimal_places=0, default=0)
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (str(self.empresa)+" "+str(self.user))


class Cliclo (models.Model):
    abreviación = models.CharField(max_length=100)
    
    def __str__(self):
        return self.abreviación


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)


class Mensaje(models.Model):
    emitido = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    recibido = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    #hilos = models.ManyToManyField('Mensaje')
    #medio = models.CharField(max_length=100)
    contenido = models.CharField(max_length=1000)
    #fmes = models.CharField(max_length=100)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)


class practica(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField(blank=True, null=True)
    fechaFin = models.DateTimeField(blank=True, null=True)
    tele = models.CharField(max_length=100)
    erasmus = models.CharField(max_length=100)


class Tool(models.Model):
    nombre = models.CharField(max_length=100)
    #lenguaje = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Requisito(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Funcion(models.Model):
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Oferta(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE)
    toolboxes = models.ManyToManyField('Tool')
    especifaciones = models.ManyToManyField('Requisito')
    competencias = models.ManyToManyField('Perfil')
    bibliotecas = models.ManyToManyField('Funcion')
    nombre = models.CharField(max_length=100)
    #fofe = models.CharField(max_length=100)
    #kas = models.CharField(max_length=100)
    #tele = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
