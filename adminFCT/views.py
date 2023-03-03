from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.hashers import make_password
from tempus_dominus.widgets import DatePicker, DateTimePicker
from django.db.models import Q

from adminFCT.models import Empresa, Contrato, Profesor, Alumno, User, Trayecto, Ciclo, Practica
from adminFCT.models import Empleado, Mensaje, Contacto, Sede, Oferta, Tool, Perfil, Funcion, Requisito
from adminFCT.models import Forma, Ramo, Tamano, Medio

import secrets
import string

#funciones

empreAlum='vacia'

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars
pwd_length = 12

def contraseña(contra):
    contra = ''
    for i in range(pwd_length):
        contra+=''.join(secrets.choice(alphabet))
    salida=make_password(contra)
    return salida

def sacar_hilo(objeto):
    if objeto.hilos:
        solu=sacar_hilo(Mensaje.objects.get(pk=objeto.hilos.pk))
        solu.append(objeto.pk)
    else:
        solu=[]
        solu.append(objeto.pk)
    return solu

def user_profesor(self):
    if self.request.user.is_teacher or self.request.user.is_staff:
        resul=True
    else:
        resul=False
    return resul

def user_estudiante(self):
    if self.request.user.is_student or self.request.user.is_staff:
        resul=True
    else:
        resul=False
    return resul

def user_contacto(self):
    if self.request.user.is_contact or self.request.user.is_staff:
        resul=True
    else:
        resul=False
    return resul

# Create your views here.

#vista de index
def index(request):
    return render(request,'adminFCT/index.html')

#vista alumno

class AlumnoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Alumno
    def get_queryset(self):
        obj=Alumno.objects.all()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class AlumnoDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Alumno
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class AlumnoSearch(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Alumno
    Template_name = 'alumno_list.html'
    def get_queryset (self):
        obj=Alumno.objects.all()
        es=user_profesor(self)
        if es:
            query = self.request.GET.get("q")
            obj = Alumno.objects.filter( Q (nomAlu__icontains=query))
            return obj
        else:
            raise PermissionDenied

#vista Forma

class FormaListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Forma
    def get_queryset(self):
        obj=Forma.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class FormaCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Forma
    success_url = reverse_lazy("forma-list")
    fields = ['desFor']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class FormaUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Forma
    success_url = reverse_lazy("forma-list")
    fields = ['desFor']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class FormaDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Forma
    success_url = reverse_lazy("forma-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vistas Ramo

class RamoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Ramo
    def get_queryset(self):
        obj=Ramo.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class RamoCrateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Ramo
    success_url = reverse_lazy('ramo-list')
    fields = ['desRam']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class RamoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Ramo
    success_url = reverse_lazy('ramo-list')
    fields = ['desRam']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class RamoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Ramo
    success_url = reverse_lazy('ramo-list')
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vistas tamano

class TamanoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Tamano
    def get_queryset(self):
        obj=Tamano.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class TamanoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Tamano
    success_url = reverse_lazy('tamano-list')
    fields = ['desTam']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class TamanoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Tamano
    success_url = reverse_lazy('tamano-list')
    fields = ['desTam']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class TamanoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Tamano
    success_url = reverse_lazy('tamano-list')
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vistas de Empresa

class EmpresaListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Empresa
    def get_queryset(self):
        obj=Empresa.objects.all().exclude(nomEmp=empreAlum)
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class EmpresaDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Empresa
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class EmpresaCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    fields = ['nomEmp','razon','web','logo', 'numTra','forma','ramo','tam']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class EmpresaUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    fields = ['nomEmp','razon','web','logo', 'numTra','forma','ramo','tam']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class EmpresaDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Empresa
    success_url= reverse_lazy("empresa-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class EmpresaSearch(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Empresa
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Empresa.objects.filter( Q (nomEmp__icontains=query)).exclude(nomEmp=empreAlum)
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied


#vistas de ciclo

class CicloListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Ciclo
    def get_queryset(self):
        obj=Ciclo.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class CicloCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Ciclo
    success_url= reverse_lazy("ciclo-list")
    fields = ['abre']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class CicloUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Ciclo
    success_url= reverse_lazy("ciclo-list")
    fields = ['abre']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class CicloDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Ciclo
    success_url = reverse_lazy("ciclo-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vista de trayecto

class TrayectoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Trayecto
    def get_queryset(self):
        obj=Trayecto.objects.all()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied
    

class TrayectoDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Trayecto
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied
    

class TrayectoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Trayecto
    success_url = reverse_lazy("trayecto-list")
    fields = ['alumno','ciclo','fpromo']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            obj.fields['fpromo'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
            return obj
        else:
            raise PermissionDenied

class TrayectoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Trayecto
    success_url = reverse_lazy("trayecto-list")
    fields = ['alumno','ciclo','fpromo']
    template_name_suffix = '_update_form'
    def get_form(self):
        form = super().get_form()
        form.fields['fpromo'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        return form
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class TrayectoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Trayecto
    success_url = reverse_lazy("trayecto-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class TrayectoSearchAlumno(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Trayecto
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Trayecto.objects.filter( Q (alumno__nomAlu__icontains=query))
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class TrayectoSearchCiclo(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Trayecto
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Trayecto.objects.filter( Q (ciclo__abre__icontains=query))
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class TrayectoSearchPromocion(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Trayecto
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Trayecto.objects.filter( Q (fpromo__icontains=query))
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied


#vista sede

class SedeListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Sede
    def get_queryset(self):
        obj=Sede.objects.all()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class SedeDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Sede
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class SedeCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Sede
    success_url = reverse_lazy("sede-list")
    fields = ['empresa','cpSed']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class SedeUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Sede
    success_url = reverse_lazy("sede-list")
    fields = ['empresa','cpSed']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class SedeDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Sede
    success_url = reverse_lazy("sede-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied


#vistas de Contacto

class ContactoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Contacto
    def get_queryset(self):
        obj=Contacto.objects.all()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class ContactoDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Contacto
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class ContactoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = User
    success_url= reverse_lazy("contacto-list")
    fields = ['username','email']
    template_name = 'adminFCT/contacto_form.html'
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        form.instance.password = contraseña('')
        form.instance.is_active = False
        form.instance.is_contact = True
        form.save()
        emple = Empleado.objects.create(nomEmp=form.instance.username)
        empre = Empresa.objects.get(nomEmp=empreAlum)
        conta = Contacto.objects.create(user=form.instance, empresa=empre, empleado=emple, mailCon=form.instance.email, movCon='000000')
        return redirect("contacto-update2", pk=conta.pk)

class ContactoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Contacto
    success_url= reverse_lazy("contacto-list")
    fields = ['empresa','empleado','mailCon']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class ContactoUpdateView2(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Contacto
    success_url= reverse_lazy("contacto-list")
    fields = ['empresa','movCon']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class ContactodeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    success_url= reverse_lazy("contacto-list")
    model = Contacto
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class ContactoSearchNombre(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Contacto
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Contacto.objects.filter( Q (empleado__nomEmp__icontains=query))
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class ContactoSearchEmpresa(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Contacto
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Contacto.objects.filter( Q (empresa__nomEmp__icontains=query))
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied


#vista para contrato

class ContratoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Contrato
    def get_queryset(self):
        obj=Contrato.objects.all()
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class ContratoDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Contrato
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class ContratoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Contrato
    success_url= reverse_lazy("contrato-list")
    fields = ['empresa','alumno','pra','iniCon','finCon']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es==True:
            obj.fields['iniCon'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            obj.fields['finCon'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        solu = super().form_valid(form)
        empre=Empresa.objects.get(nomEmp=empreAlum)
        if form.instance.empresa == empre:
            form.add_error("empresa","Esta empresa no es valida.")
            solu = super().form_invalid(form)
        return solu

class ContratoAlumnoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Contrato
    success_url= reverse_lazy("contrato-list")
    fields = ['empresa','pra','iniCon','finCon']
    def get_form(self):
        obj=super().get_form()
        estu=user_estudiante(self)
        if estu==True:
            obj.fields['iniCon'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            obj.fields['finCon'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        alumno = Alumno.objects.get(user=self.request.user)
        form.instance.alumno = alumno
        solu = super().form_valid(form)
        empre=Empresa.objects.get(nomEmp=empreAlum)
        if form.instance.empresa == empre:
            form.add_error("empresa","Esta empresa no es valida.")
            solu = super().form_invalid(form)
        return solu

class ContratoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Contrato
    success_url= reverse_lazy("contrato-list")
    fields = ['empresa','alumno','pra','iniCon','finCon']
    template_name_suffix = '_update_form'
    def get_form(self):
        form = super().get_form()
        form.fields['iniCon'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        form.fields['finCon'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        return form
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        estu=user_estudiante(self)
        if not self.request.user == obj.alumno.user:
            estu=False
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        solu = super().form_valid(form)
        empre = Empresa.objects.get(nomEmp=empreAlum)
        if self.request.user.is_student:
            alumno = Alumno.objects.get(user=self.request.user)
            if not form.instance.alumno == alumno:
                form.add_error("alumno","No puedes cambiar el alumno de este contrato.")
                solu = super().form_invalid(form)
        if form.instance.empresa == empre:
            form.add_error("empresa","Esta empresa no es valida.")
            solu = super().form_invalid(form)
        return solu
    

class ContratoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Contrato
    success_url= reverse_lazy("contrato-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        estu=user_estudiante(self)
        if not self.request.user == obj.alumno.user:
            estu=False
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class ContratoSearchAlumno(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Contrato
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Contrato.objects.filter( Q (alumno__nomAlu__icontains=query))
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class ContratoSearchEmpresa(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Contrato
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Contrato.objects.filter( Q (empresa__nomEmp__icontains=query))
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied


#vistas para medio

class MedioListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Medio
    def get_queryset(self):
        obj=Medio.objects.all()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class MedioCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Medio
    success_url= reverse_lazy("medio-list")
    fields = ['nomMed']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class MedioUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Medio
    success_url= reverse_lazy("medio-list")
    fields = ['nomMed']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class MedioDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Medio
    success_url= reverse_lazy("medio-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied


#vista para mensaje

class MensajeListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Mensaje
    def get_queryset(self):
        obj=Mensaje.objects.all().order_by("-id")
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        contex = super(MensajeListView, self).get_context_data(**kwargs)
        descartados = []
        object_list = Mensaje.objects.all()
        for objeto in object_list:
            if objeto.mensaje_set.all():
                descartados.append(objeto.pk)
        contex['descartados'] = descartados
        return contex

class MensajeDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Mensaje
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        contex = super(MensajeDetailView, self).get_context_data(**kwargs)
        lista=sacar_hilo(self.get_object())
        lista.pop(-1)
        relista=[]
        for numero in lista:
            relista.append(Mensaje.objects.get(pk=numero))
        contex['relista']=relista
        return contex

class MensajeCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Mensaje
    success_url= reverse_lazy("mensaje-list")
    fields = ['emitido','recibido','medio','conte','fmen']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            obj.fields['fmen'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
            return obj
        else:
            raise PermissionDenied

class MensajeRespuestaCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Mensaje
    #success_url= reverse_lazy("mensaje-list")
    fields = ['emitido','conte','fmen']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            obj.fields['fmen'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        url=self.request.get_full_path()
        urllist=url.split("/")
        objeto=Mensaje.objects.get(pk=int(urllist[2]))
        if objeto.mensaje_set.all():
            form.add_error("emitido","ya se ha respondido a este mensaje.")
            sali = super().form_invalid(form)
        else:
            form.instance.hilos = objeto
            form.instance.medio = objeto.medio
            form.instance.recibido = objeto.emitido
            solu = form.save()
            sali = redirect("mensaje-detail", pk=solu.id)
        return sali

class MensajeUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Mensaje
    success_url= reverse_lazy("mensaje-list")
    fields = ['emitido','recibido','medio','hilos','conte','fmen']
    template_name_suffix = '_update_form'
    def get_form(self):
        form = super().get_form()
        form.fields['fmen'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        return form
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            
            return obj
        else:
            raise PermissionDenied

class MensajeDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Mensaje
    success_url= reverse_lazy("mensaje-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class MensajeSearch(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Mensaje
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Mensaje.objects.filter( Q (recibido__nomEmp__icontains=query) | Q(emitido__nomEmp__icontains=query)).order_by("-id")
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        contex = super(MensajeSearch, self).get_context_data(**kwargs)
        descartados = []
        object_list = Mensaje.objects.all()
        for objeto in object_list:
            if objeto.mensaje_set.all():
                descartados.append(objeto.pk)
        contex['descartados'] = descartados
        return contex


#vistas para practica

class PracticaListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Practica
    def get_queryset(self):
        obj=Practica.objects.all()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class PracticaDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Practica
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class PracticaCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Practica
    success_url= reverse_lazy("practica-list")
    fields = ['alumno','ciclo','contacto','fIni','fFin','tele','E']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es:
            obj.fields['fIni'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            obj.fields['fFin'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        profesor = Profesor.objects.get(user=self.request.user)
        form.instance.profesor=profesor
        return super().form_valid(form)

class PracticaUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Practica
    success_url= reverse_lazy("practica-list")
    fields = ['alumno','ciclo','profesor','contacto','fIni','fFin','tele','E']
    template_name_suffix = '_update_form'
    def get_form(self):
        form = super().get_form()
        form.fields['fIni'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        form.fields['fFin'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        return form
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class PracticaDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Practica
    success_url= reverse_lazy("practica-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es:
            return obj
        else:
            raise PermissionDenied

class PracticaSearchAlumno(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Practica
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Practica.objects.filter( Q (alumno__nomAlu__icontains=query))
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied

class PracticaSearchCiclo(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Practica
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Practica.objects.filter( Q (ciclo__abre__icontains=query))
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied

class PracticaSearchProfesor(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Practica
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Practica.objects.filter( Q (profesor__empleado__nomEmp__icontains=query))
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied

class PracticaSearchContacto(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Practica
    def get_queryset(self):
        query = self.request.GET.get("q")
        obj = Practica.objects.filter( Q (contacto__empleado__nomEmp__icontains=query))
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied


#url para tool

class ToolListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Tool
    def get_queryset(self):
        obj=Tool.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class ToolCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Tool
    success_url= reverse_lazy("tool-list")
    fields = ['nomToo','lenguaje']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class ToolUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Tool
    success_url= reverse_lazy("tool-list")
    fields = ['nomToo','lenguaje']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class ToolDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Tool
    success_url= reverse_lazy("tool-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vistas para requisito

class RequisitoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Requisito
    def get_queryset(self):
        obj=Requisito.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class RequisitoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Requisito
    success_url= reverse_lazy("requisito-list")
    fields = ['nomReq']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class RequisitoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Requisito
    success_url= reverse_lazy("requisito-list")
    fields = ['nomReq']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class RequisitoDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Requisito
    success_url= reverse_lazy("requisito-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vista para perfil

class PerfilListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Perfil
    def get_queryset(self):
        obj=Perfil.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class PerfilCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Perfil
    success_url= reverse_lazy("perfil-list")
    fields = ['nomPer']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class PerfilUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Perfil
    success_url= reverse_lazy("perfil-list")
    fields = ['nomPer']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class PerfilDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Perfil
    success_url= reverse_lazy("perfil-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#vistas para funcion

class FuncionListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Funcion
    def get_queryset(self):
        obj=Funcion.objects.all()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class FuncionCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Funcion
    success_url= reverse_lazy("funcion-list")
    fields = ['perfil','nomFun']
    def get_form(self):
        obj=super().get_form()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class FuncionUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Funcion
    success_url= reverse_lazy("funcion-list")
    fields = ['perfil','nomFun']
    template_name_suffix = '_update_form'
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied

class FuncionDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Funcion
    success_url= reverse_lazy("funcion-list")
    def get_object(self):
        obj=super().get_object()
        if self.request.user.is_staff:
            return obj
        else:
            raise PermissionDenied


#url para oferta

class OfertaListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Oferta
    def get_queryset(self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        obj=Oferta.objects.all().exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        contex = super(OfertaListView, self).get_context_data(**kwargs)
        contex['form']=True
        return contex

class OfertaAlumnoListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Oferta
    def get_queryset(self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        obj=Oferta.objects.filter(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied


class OfertaDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Oferta
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class OfertaCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Oferta
    success_url= reverse_lazy("oferta-list")
    fields = ['empresa','contacto','toolboxes','especifaciones','competencias','bibliotecas','nomOfe','fofe','kas','tele']
    def get_form(self):
        obj=super().get_form()
        es=user_profesor(self)
        if es==True:
            obj.fields['fofe'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        solu = super().form_valid(form)
        if not form.instance.empresa and not form.instance.contacto:
            form.add_error("empresa","Debe de tener al menos una empresa o un contacto seleccionado.")
            solu = super().form_invalid(form)
        empre=Empresa.objects.get(nomEmp=empreAlum)
        if form.instance.empresa == empre:
            form.add_error("empresa","Esta empresa no es valida.")
            solu = super().form_invalid(form)
        return solu

class OfertaAlumnoCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Oferta
    success_url= reverse_lazy("oferta-list")
    fields = ['toolboxes','especifaciones','competencias','bibliotecas','nomOfe','fofe','kas','tele']
    def get_form(self):
        obj=super().get_form()
        es=user_estudiante(self)
        if es==True:
            obj.fields['fofe'].widget = DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                })
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        empre=Empresa.objects.get(nomEmp=empreAlum)
        form.instance.empresa=empre
        return super().form_valid(form)

class OfertaUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = Oferta
    success_url= reverse_lazy("oferta-list")
    fields = ['empresa','contacto','toolboxes','especifaciones','competencias','bibliotecas','nomOfe','fofe','kas','tele']
    template_name_suffix = '_update_form'
    def get_form(self):
        form = super().get_form()
        form.fields['fofe'].widget = DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            })
        return form
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied
    def form_valid(self, form):
        solu = super().form_valid(form)
        print(form.instance.empresa)
        if not form.instance.empresa and not form.instance.contacto:
            form.add_error("empresa","Debe de tener al menos una empresa o un contacto seleccionado.")
            solu = super().form_invalid(form)
        empre=Empresa.objects.get(nomEmp=empreAlum)
        if form.instance.empresa == empre:
            form.add_error("empresa","Esta empresa no es valida.")
            solu = super().form_invalid(form)
        return solu

class OfertaDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Oferta
    success_url= reverse_lazy("oferta-list")
    def get_object(self):
        obj=super().get_object()
        es=user_profesor(self)
        if es==True:
            return obj
        else:
            raise PermissionDenied

class OfertaSearchNombre(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Oferta
    Template_name = 'oferta_list.html'
    def get_queryset (self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        query = self.request.GET.get("q")
        obj = Oferta.objects.filter( Q (nomOfe__icontains=query)).exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class OfertaSearchEmpresa(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Oferta
    Template_name = 'oferta_list.html'
    def get_queryset (self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        query = self.request.GET.get("q")
        obj = Oferta.objects.filter( Q (empresa__nomEmp__icontains=query)).exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class OfertaSearchContacto(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Oferta
    Template_name = 'oferta_list.html'
    def get_queryset (self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        query = self.request.GET.get("q")
        obj = Oferta.objects.filter( Q (contacto__empleado__nomEmp__icontains=query)).exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class OfertaSearchRequisito(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Oferta
    Template_name = 'oferta_list.html'
    def get_queryset (self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        query = self.request.GET.get("q")
        obj = Oferta.objects.filter( Q (especifaciones__nomReq__icontains=query)).exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class OfertaSearchPerfil(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Oferta
    Template_name = 'oferta_list.html'
    def get_queryset (self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        query = self.request.GET.get("q")
        obj = Oferta.objects.filter( Q (competencias__nomPer__icontains=query)).exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied

class OfertaSearchFuncion(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Oferta
    Template_name = 'oferta_list.html'
    def get_queryset (self):
        quitar=Empresa.objects.get(nomEmp=empreAlum)
        query = self.request.GET.get("q")
        obj = Oferta.objects.filter( Q (bibliotecas__nomFun__icontains=query)).exclude(empresa=quitar).order_by("-id")
        es=user_profesor(self)
        estu=user_estudiante(self)
        if es==True or estu==True:
            return obj
        else:
            raise PermissionDenied