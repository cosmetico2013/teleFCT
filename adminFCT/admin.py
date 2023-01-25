from django.contrib import admin
from adminFCT.models import Empresa, Contrato, Profesor, Alumno, User

# Register your models here.
admin.site.register(Empresa)
admin.site.register(User)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Contrato)