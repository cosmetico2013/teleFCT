from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)


class Profesor(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    nomAlu = models.CharField(max_length=100)
    movil = models.CharField(max_length=20)
    mail = models.EmailField()
    curri = models.URLField() #curriculum
    proy = models.URLField() #direccion de github
    fnac = models.DateTimeField() #fecha de nacimiento
    sex = models.CharField(max_length=1)
    dis = models.DecimalField(max_digits=3, decimal_places=0, default=0) #discapacidad en porcentaje
    cpAlu = models.DecimalField(max_digits=20, decimal_places=0, default=0)

    def __str__(self):
        return self.nomAlu


class Forma(models.Model):
    desFor = models.CharField(max_length=15)

    def __str__(self):
        return self.desFor


class Ramo(models.Model):
    desRam = models.CharField(max_length=50)

    def __str__(self):
        return self.desRam


class Tamano(models.Model): #tamaños de las empresas
    desTam = models.CharField(max_length=15)

    def __str__(self):
        return self.desTam


class Empresa(models.Model):
    forma = models.ForeignKey('Forma', on_delete=models.SET_NULL, null=True)
    ramo = models.ForeignKey('Ramo', on_delete=models.SET_NULL, null=True)
    tam = models.ForeignKey('Tamano', on_delete=models.SET_NULL, null=True)
    nomEmp = models.CharField(max_length=100)
    logo = models.FileField(upload_to="img/", null=True, blank=True)
    razon = models.CharField(max_length=100) #es la razon social, nombre que tiene la empresa en el registro
    numTra = models.DecimalField(max_digits=10, decimal_places=0, default=0) #numero de trabajadores
    web = models.URLField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return str(self.nomEmp)


class Ciclo(models.Model):
    abre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.abre    


class Trayecto(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    fpromo = models.DateTimeField()

    def __str__(self):
        #return self.alumno+' '+self.ciclo.abre
        return self.alumno


class Sede(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    cpsed = models.DecimalField(max_digits=20, decimal_places=0, default=0)

    def __str__(self):
        return self.empresa.nomEmp+' '+str(self.cpsed)


class Contacto (models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    mailCon = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Contrato (models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    pra = models.BooleanField() #si es en practica
    iniCon = models.DateTimeField(blank=True, null=True)
    finCon = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (str(self.empresa)+" "+str(self.alumno))


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)


class Medio(models.Model): # medio por el que se envio el mensaje
    nomMed = models.CharField(max_length=20)

    def __str__(self):
        return self.nomMed


class Mensaje(models.Model):
    #emitido = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    recibido = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    medio = models.ForeignKey('Medio', on_delete=models.SET_NULL, null=True)
    hilos = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    contenido = models.CharField(max_length=1000)
    fmen = models.DateTimeField(blank=True, null=True) #fecha del mensaje 


class Practica(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField(blank=True, null=True)
    fechaFin = models.DateTimeField(blank=True, null=True)
    tele = models.BooleanField() #si es un teletravajo
    erasmus = models.BooleanField() #si es un erasmus



class Tool(models.Model): #las erramientas que prorciona
    nombre = models.CharField(max_length=100)
    lenguaje = models.CharField(max_length=1) #S es un lenguaje o N si no lo es

    def __str__(self):
        return self.nombre


class Requisito(models.Model): #
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
    fofe = models.DateTimeField(blank=True, null=True) #Fecha de oferta
    kas = models.DecimalField(max_digits=10, decimal_places=2, default=0) #salario anual
    tele = models.BooleanField() #teletravajo 

    def __str__(self):
        return self.nombre
