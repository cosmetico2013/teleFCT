from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_contact = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Empleado(models.Model):
    nomEmp = models.CharField(max_length=100)

    def __str__(self):
        return self.nomEmp

class Profesor(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    empleado = models.OneToOneField('Empleado', on_delete=models.CASCADE)

    def __str__(self):
        return self.empleado.nomEmp

class Distrito(models.Model):
    cp = models.CharField(verbose_name='codigo postal', max_length=15, unique=True)
    distri = models.CharField(verbose_name='distrito', max_length=70)

    def __str__(self):
        return self.cp+" "+self.distri

class Alumno(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    cpAlu = models.ForeignKey('Distrito', on_delete=models.CASCADE)
    nomAlu = models.CharField(max_length=100)
    movil = models.CharField(max_length=20, blank=True, null=True)
    mail = models.EmailField()
    curri = models.URLField(blank=True, null=True) #curriculum
    proy = models.URLField(blank=True, null=True) #direccion de github
    fnac = models.DateField() #fecha de nacimiento
    sex = models.CharField(max_length=1)
    dis = models.DecimalField(max_digits=3, decimal_places=0, default=0) #discapacidad en porcentaje

    def __str__(self):
        return self.nomAlu


class Forma(models.Model):
    desFor = models.CharField(verbose_name='forma', max_length=15)

    def __str__(self):
        return self.desFor


class Ramo(models.Model):
    desRam = models.CharField(verbose_name='rama', max_length=50)

    def __str__(self):
        return self.desRam


class Tamano(models.Model): #tamaños de las empresas
    desTam = models.CharField(verbose_name='Tamaño', max_length=15)

    def __str__(self):
        return self.desTam


class Empresa(models.Model):
    forma = models.ForeignKey('Forma',verbose_name='forma',  on_delete=models.SET_NULL, null=True)
    ramo = models.ForeignKey('Ramo',verbose_name='rama',  on_delete=models.SET_NULL, null=True)
    tam = models.ForeignKey('Tamano',verbose_name='tamaño',  on_delete=models.SET_NULL, null=True)
    nomEmp = models.CharField(verbose_name='Nombre', max_length=100)
    logo = models.FileField(upload_to="img/")
    razon = models.CharField(max_length=100) #es la razon social, nombre que tiene la empresa en el registro
    numTra = models.DecimalField(verbose_name='numero de trabajadores', max_digits=10, decimal_places=0, default=0) #numero de trabajadores
    web = models.URLField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return str(self.nomEmp)


class Ciclo(models.Model):
    abre = models.CharField(verbose_name='abreviación', max_length=100, unique=True)
    
    def __str__(self):
        return self.abre    


class Trayecto(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    fpromo = models.DateField(verbose_name='Promocion', null=True, blank=True)

    def __str__(self):
        #return self.alumno+' '+self.ciclo.abre
        return self.alumno


class Sede(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    cpSed = models.ForeignKey('Distrito',verbose_name='codigo postal', on_delete=models.CASCADE)

    def __str__(self):
        return self.empresa.nomEmp+' '+str(self.cpSed)


class Contacto (models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    empleado = models.OneToOneField('Empleado', on_delete=models.CASCADE)
    mailCon = models.EmailField(verbose_name='Correo')
    movCon = models.CharField(verbose_name='movil', max_length=20, blank=True, null=True) #movil de contacto

    def __str__(self):
        return self.empleado.nomEmp
        #return self.nombre


class Contrato (models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    pra = models.BooleanField(verbose_name='practica') #si es en practica
    iniCon = models.DateField(verbose_name='inicio', blank=True, null=True)
    finCon = models.DateField(verbose_name='fin', blank=True, null=True)

    def __str__(self):
        return (str(self.empresa)+" "+str(self.alumno))


class Medio(models.Model): # medio por el que se envio el mensaje
    nomMed = models.CharField(max_length=20)

    def __str__(self):
        return self.nomMed


class Mensaje(models.Model):
    emitido = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='emitido')
    recibido = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='recibido')
    medio = models.ForeignKey('Medio', on_delete=models.SET_NULL, null=True)
    hilos = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    conte = models.CharField(verbose_name='contenido', max_length=1000) #contenido
    fmen = models.DateField(verbose_name='fecha', blank=True, null=True) #fecha del mensaje 

    def __str__(self):
        return self.emitido.nomEmp+' '+self.recibido.nomEmp


class Practica(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE)
    fIni = models.DateField(verbose_name='inicio') #fecha de inicio
    fFin = models.DateField(verbose_name='fin') #fecha de fin
    tele = models.BooleanField(verbose_name='teletrabajo') #si es un teletravajo
    E = models.BooleanField(verbose_name='erasmus', ) #si es un erasmus

    def __str__(self):
        return self.alumno.nomAlu+' '+self.ciclo.abre



class Tool(models.Model): #las erramientas que prorciona
    nomToo = models.CharField(verbose_name='herramienta', max_length=100)
    lenguaje = models.BooleanField(verbose_name='Lenguaje de programacion')

    def __str__(self):
        return self.nomToo


class Requisito(models.Model): #
    nomReq = models.CharField(verbose_name='requisito', max_length=100)

    def __str__(self):
        return self.nomReq


class Perfil(models.Model):
    nomPer = models.CharField(verbose_name='perfil', max_length=100)

    def __str__(self):
        return self.nomPer


class Funcion(models.Model):
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE)
    nomFun = models.CharField(verbose_name='funcion', max_length=100)

    def __str__(self):
        return self.nomFun


class Oferta(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE, null=True, blank=True)
    toolboxes = models.ManyToManyField('Tool',verbose_name='Herramientas')
    especifaciones = models.ManyToManyField('Requisito', verbose_name='Requisitos')
    competencias = models.ManyToManyField('Perfil', verbose_name='Perfiles')
    bibliotecas = models.ManyToManyField('Funcion', verbose_name='funciones')
    nomOfe = models.CharField(verbose_name='nombre', max_length=100)
    fofe = models.DateField(verbose_name='Fecha', blank=True, null=True) #Fecha de oferta
    kas = models.DecimalField(verbose_name='dinero', max_digits=10, decimal_places=0, null=True, blank=True) #salario anual
    tele = models.BooleanField(verbose_name='teletrabajo') #teletrabajo 

    def __str__(self):
        return self.nomOfe
