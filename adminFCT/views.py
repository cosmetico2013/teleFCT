from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from adminFCT.models import Empresa, Contacto, Contrato

# Create your views here.

#vista de index
def index(request):
    return render(request,'adminFCT/index.html')


#vistas de Empresa

class EmpresaListView(ListView):
    model = Empresa

class EmpresaDetailView(DetailView):
    model = Empresa

class EmpresaCreateView(CreateView):
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    fields = ['nombre']

class EmpresaUpdateView(UpdateView):
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    fields = ['nombre']
    template_name_suffix = '_update_form'

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url= reverse_lazy("empresa-list")



#vistas de Contacto

class ContactosDetailView(DetailView):
    model = Contacto

class ContactosCreateView(CreateView):
    model = Contacto
    success_url= reverse_lazy("empresa-list")
    fields = ['nombre', 'apellidos', 'telefono', 'correo', 'puesto', 'empresa']

class ContactosUpdateView(UpdateView):
    model = Contacto
    success_url= reverse_lazy("empresa-list")
    fields = ['nombre','apellidos','telefono','correo','puesto','empresa']
    template_name_suffix = '_update_form'

class ContactosdelteView(DeleteView):
    success_url= reverse_lazy("empresa-list")
    model = Contacto



# 
