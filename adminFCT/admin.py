from django.contrib import admin
from adminFCT.models import Empresa, Intereses, Contactos, Busca, Contrato

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Intereses)
admin.site.register(Contactos)
admin.site.register(Busca)
admin.site.register(Contrato)