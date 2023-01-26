from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.shortcuts import redirect

from adminFCT.models import Empresa, Contrato, Profesor, Alumno, User, Trayectos, Ciclo, Practica
from adminFCT.models import Empleado, Mensaje, Contacto, Sede, Oferta, Tool, Perfil, Funcion, Requisito
from adminFCT.models import Forma, Ramo, Tamano, Medio

from teleFCT.forms import ProfesorSignUpForm

# Create your views here.

#login profesor
class ProfesorSignUpView(CreateView):
    model = User
    form_class = ProfesorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Profesor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


#vista de index
def index(request):
    return render(request,'adminFCT/index.html')

#vista alumno

class AlumnoListView(ListView):
    model = Alumno

class AlumnoDetailView(DetailView):
    model = Alumno


#vista Forma

class FormaListView(ListView):
    model = Forma

class FormaCreateView(CreateView):
    model = Forma
    success_url = reverse_lazy("forma-list")
    fields = ['desFor']

class FormaUpdateView(UpdateView):
    model = Forma
    success_url = reverse_lazy("forma-list")
    fields = ['desFor']
    template_name_suffix = '_update_form'

class FormaDeleteView(DeleteView):
    model = Forma
    success_url = reverse_lazy("forma-list")


#vistas Ramo

class RamoListView(ListView):
    model = Ramo

class RamoCrateView(CreateView):
    model = Ramo
    success_url = reverse_lazy('ramo-list')
    fields = ['desRam']

class RamoUpdateView(UpdateView):
    model = Ramo
    success_url = reverse_lazy('ramo-list')
    fields = ['desRam']
    template_name_suffix = '_update_form'

class RamoDeleteView(DeleteView):
    model = Ramo
    success_url = reverse_lazy('ramo-list')


#vistas tamano

class TamanoListView(ListView):
    model = Tamano

class TamanoCreateView(CreateView):
    model = Tamano
    success_url = reverse_lazy('tamano-list')
    fields = ['desTam']

class TamanoUpdateView(UpdateView):
    model = Tamano
    success_url = reverse_lazy('tamano-list')
    fields = ['desTam']
    template_name_suffix = '_update_form'

class TamanoDeleteView(DeleteView):
    model = Tamano
    success_url = reverse_lazy('tamano-list')


#vistas de Empresa

class EmpresaListView(ListView):
    model = Empresa

class EmpresaDetailView(DetailView):
    model = Empresa

class EmpresaCreateView(CreateView):
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    fields = ['nomEmp','razon','web','logo', 'numTra','forma','ramo','tam']

class EmpresaUpdateView(UpdateView):
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    fields = ['nomEmp','razon','web','logo', 'numTra','forma','ramo','tam']
    template_name_suffix = '_update_form'

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url= reverse_lazy("empresa-list")


#vistas de ciclo

class CicloListView(ListView):
    model = Ciclo

class CicloCreateView(CreateView):
    model = Ciclo
    success_url= reverse_lazy("ciclo-list")
    fields = ['abre']

class CicloUpdateView(UpdateView):
    model = Ciclo
    success_url= reverse_lazy("ciclo-list")
    fields = ['abre']
    template_name_suffix = '_update_form'    

class CicloDeleteView(DeleteView):
    model = Ciclo
    success_url= reverse_lazy("ciclo-list")


#vistas de Contacto

class ContactosDetailView(DetailView):
    model = Contacto

class ContactosCreateView(CreateView):
    model = Contacto
    success_url= reverse_lazy("empresa-list")
    fields = ['movcon']

class ContactosUpdateView(UpdateView):
    model = Contacto
    success_url= reverse_lazy("empresa-list")
    fields = ['nombre','apellidos','telefono','correo','puesto','empresa']
    template_name_suffix = '_update_form'

class ContactosdeleteView(DeleteView):
    success_url= reverse_lazy("empresa-list")
    model = Contacto
