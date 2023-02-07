from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.shortcuts import redirect

from adminFCT.models import Empresa, Contrato, Profesor, Alumno, User, Trayecto, Ciclo, Practica
from adminFCT.models import Empleado, Mensaje, Contacto, Sede, Oferta, Tool, Perfil, Funcion, Requisito
from adminFCT.models import Forma, Ramo, Tamano, Medio

from teleFCT.forms import ProfesorSignUpForm , registro

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

class registroview(CreateView):
    model = User
    form_class = registro
    template_name = 'registration/signup_form.html'

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
    success_url = reverse_lazy("ciclo-list")


#vista de trayecto

class TrayectoListView(ListView):
    model = Trayecto

class TrayectoDetailView(DetailView):
    model = Trayecto

class TrayectoCreateView(CreateView):
    model = Trayecto
    success_url = reverse_lazy("trayecto-list")
    fields = ['alumno','ciclo','fpromo']

class TrayectoUpdateView(UpdateView):
    model = Trayecto
    success_url = reverse_lazy("trayecto-list")
    fields = ['alumno','ciclo','fpromo']
    template_name_suffix = '_update_form'

class TrayectoDeleteView(DeleteView):
    model = Trayecto
    success_url = reverse_lazy("trayecto-list")


#vista sede

class SedeListView(ListView):
    model = Sede

class SedeDetailView(DetailView):
    model = Sede    

class SedeCreateView(CreateView):
    model = Sede
    success_url = reverse_lazy("sede-list")
    fields = ['empresa','cpsed']

class SedeUpdateView(UpdateView):
    model = Sede
    success_url = reverse_lazy("sede-list")
    fields = ['empresa','cpsed']
    template_name_suffix = '_update_form'

class SedeDeleteView(DeleteView):
    model = Sede
    success_url = reverse_lazy("sede-list")


#vistas de Contacto

class ContactoListView(ListView):
    model = Contacto

class ContactoDetailView(DetailView):
    model = Contacto

from teleFCT.forms import ContactoForm, ContactoForm2

class ContactoCreateView(CreateView):
    model = Contacto
    success_url= reverse_lazy("contacto-list")
    #fields = ['empresa','empleado','mailCon']
    form_class = ContactoForm
    second_form_class = ContactoForm2
    def get_context_data(self, **kwargs):
        context = super(ContactoCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    def form_valid(self, form):
        print('valid')
        print(form.instance)
        return super().form_valid(form)

    '''def form_valid(self, form):
        print(form)
        return redirect('contacto-add')'''

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form.is_valid()
        print('request')
        print(request)
        p = super().post(request, *args, **kwargs)
        print('post')
        print(p)
        return redirect('contacto-add')
'''
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        #if form.is_valid() and form2.is_valid():
        #p = Empleado.objects.create(nomEmp=form2.nomEmp)
        #print(p.pk)
        form_valid(form)
        form2.is_valid()

        return redirect('contacto-add')

        else:
            print('no')
            return redirect('contacto-add')
    
    def get_form(self):
        form=super().get_form()
        print(form)
        print('hola-que-tal')
        #print(form.add.)
        return form
    def form_valid(self, form):
        fin=super().form_valid(form)
        print(form.instance.nombre)
        return fin
    '''

class ContactoUpdateView(UpdateView):
    model = Contacto
    success_url= reverse_lazy("contacto-list")
    fields = ['empresa','empleado','mailCon']
    template_name_suffix = '_update_form'

class ContactodeleteView(DeleteView):
    success_url= reverse_lazy("contacto-list")
    model = Contacto


#vista para contrato

class ContratoListView(ListView):
    model = Contrato

class ContratoDetailView(DetailView):
    model = Contrato

class ContratoCreateView(CreateView):
    model = Contrato
    success_url= reverse_lazy("contrato-list")
    fields = ['empresa','alumno','pra','iniCon','finCon']

class ContratoUpdateView(UpdateView):
    model = Contrato
    success_url= reverse_lazy("contrato-list")
    fields = ['empresa','alumno','pra','iniCon','finCon']
    template_name_suffix = '_update_form'

class ContratoDeleteView(DeleteView):
    model = Contrato
    success_url= reverse_lazy("contrato-list")


#vistas para medio

class MedioListView(ListView):
    model = Medio

class MedioCreateView(CreateView):
    model = Medio
    success_url= reverse_lazy("medio-list")
    fields = ['nomMed']

class MedioUpdateView(UpdateView):
    model = Medio
    success_url= reverse_lazy("medio-list")
    fields = ['nomMed']
    template_name_suffix = '_update_form'

class MedioDeleteView(DeleteView):
    model = Medio
    success_url= reverse_lazy("medio-list")


#vista para mensaje

class MensajeListView(ListView):
    model = Mensaje
    def get_queryset (self): 
        object_list = Mensaje.objects.filter( hilos__isnull=True)
        return object_list    

class MensajeDetailView(DetailView):
    model = Mensaje

class MensajeCreateView(CreateView):
    model = Mensaje
    success_url= reverse_lazy("mensaje-list")
    fields = ['emitido','recibido','medio','hilos','conte','fmen']

class MensajeUpdateView(UpdateView):
    model = Mensaje
    success_url= reverse_lazy("mensaje-list")
    fields = ['emitido','recibido','medio','hilos','conte','fmen']
    template_name_suffix = '_update_form'

class MensajeDeleteView(DeleteView):
    model = Mensaje
    success_url= reverse_lazy("mensaje-list")


#vistas para practica

class PracticaListView(ListView):
    model = Practica

class PracticaDetailView(DetailView):
    model = Practica

class PracticaCreateView(CreateView):
    model = Practica
    success_url= reverse_lazy("practica-list")
    fields = ['alumno','ciclo','contacto','fIni','fFin','tele','E']
    def form_valid(self, form):
        profesor = Profesor.objects.get(user=self.request.user)
        form.instance.profesor=profesor
        return super().form_valid(form)

class PracticaUpdateView(UpdateView):
    model = Practica
    success_url= reverse_lazy("practica-list")
    fields = ['alumno','ciclo','profesor','contacto','fIni','fFin','tele','E']
    template_name_suffix = '_update_form'

class PracticaDeleteView(DeleteView):
    model = Practica
    success_url= reverse_lazy("practica-list")


#url para tool

class ToolListView(ListView):
    model = Tool

class ToolCreateView(CreateView):
    model = Tool
    success_url= reverse_lazy("tool-list")
    fields = ['nomToo','lenguaje']

class ToolUpdateView(UpdateView):
    model = Tool
    success_url= reverse_lazy("tool-list")
    fields = ['nomToo','lenguaje']
    template_name_suffix = '_update_form'

class ToolDeleteView(DeleteView):
    model = Tool
    success_url= reverse_lazy("tool-list")


#vistas para requisito

class RequisitoListView(ListView):
    model = Requisito

class RequisitoCreateView(CreateView):
    model = Requisito
    success_url= reverse_lazy("requisito-list")
    fields = ['nomReq']

class RequisitoUpdateView(UpdateView):
    model = Requisito
    success_url= reverse_lazy("requisito-list")
    fields = ['nomReq']
    template_name_suffix = '_update_form'

class RequisitoDeleteView(DeleteView):
    model = Requisito
    success_url= reverse_lazy("requisito-list")


#vista para perfil

class PerfilListView(ListView):
    model = Perfil

class PerfilCreateView(CreateView):
    model = Perfil
    success_url= reverse_lazy("perfil-list")
    fields = ['nomPer']

class PerfilUpdateView(UpdateView):
    model = Perfil
    success_url= reverse_lazy("perfil-list")
    fields = ['nomPer']
    template_name_suffix = '_update_form'

class PerfilDeleteView(DeleteView):
    model = Perfil
    success_url= reverse_lazy("perfil-list")


#vistas para funcion

class FuncionListView(ListView):
    model = Funcion

class FuncionCreateView(CreateView):
    model = Funcion
    success_url= reverse_lazy("funcion-list")
    fields = ['perfil','nomFun']

class FuncionUpdateView(UpdateView):
    model = Funcion
    success_url= reverse_lazy("funcion-list")
    fields = ['perfil','nomFun']
    template_name_suffix = '_update_form'

class FuncionDeleteView(DeleteView):
    model = Funcion
    success_url= reverse_lazy("funcion-list")


#url para oferta

class OfertaListView(ListView):
    model = Oferta

class OfertaDetailView(DetailView):
    model = Oferta

class OfertaCreateView(CreateView):
    model = Oferta
    success_url= reverse_lazy("oferta-list")
    fields = ['empresa','contacto','toolboxes','especifaciones','competencias','bibliotecas','nomOfe','fofe','kas','tele']

class OfertaUpdateView(UpdateView):
    model = Oferta
    success_url= reverse_lazy("oferta-list")
    fields = ['empresa','contacto','toolboxes','especifaciones','competencias','bibliotecas','nomOfe','fofe','kas','tele']
    template_name_suffix = '_update_form'

class OfertaDeleteView(DeleteView):
    model = Oferta
    success_url= reverse_lazy("oferta-list")