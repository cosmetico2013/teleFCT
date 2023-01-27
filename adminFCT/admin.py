from django.contrib import admin
from adminFCT.models import Empresa, Contrato, Profesor, Alumno, User, Trayecto, Ciclo, Practica
from adminFCT.models import Empleado, Mensaje, Contacto, Sede, Oferta, Tool, Perfil, Funcion, Requisito
from adminFCT.models import Forma, Ramo, Tamano, Medio

# Register your models here.
admin.site.register(Empresa)
admin.site.register(User)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Contrato)
admin.site.register(Trayecto)
admin.site.register(Ciclo)
admin.site.register(Practica)
admin.site.register(Empleado)
admin.site.register(Mensaje)
admin.site.register(Contacto)
admin.site.register(Sede)
admin.site.register(Oferta)
admin.site.register(Tool)
admin.site.register(Perfil)
admin.site.register(Funcion)
admin.site.register(Requisito)
admin.site.register(Forma)
admin.site.register(Ramo)
admin.site.register(Tamano)
admin.site.register(Medio)