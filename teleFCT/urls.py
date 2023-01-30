"""teleFCT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from adminFCT.views import index
from adminFCT.views import AlumnoListView, AlumnoDetailView
from adminFCT.views import ContactosCreateView, ContactosdeleteView, ContactosDetailView, ContactosUpdateView
from adminFCT.views import FormaListView, FormaCreateView, FormaUpdateView, FormaDeleteView
from adminFCT.views import RamoListView, RamoCrateView, RamoUpdateView, RamoDeleteView
from adminFCT.views import TamanoListView, TamanoCreateView, TamanoUpdateView, TamanoDeleteView
from adminFCT.views import EmpresaDeleteView, EmpresaDetailView, EmpresaListView, EmpresaCreateView, EmpresaUpdateView
from adminFCT.views import CicloListView, CicloCreateView, CicloUpdateView, CicloDeleteView
from adminFCT.views import TrayectoListView, TrayectoDetailView, TrayectoCreateView, TrayectoUpdateView, TrayectoDeleteView
from adminFCT.views import SedeListView, SedeDetailView, SedeCreateView, SedeUpdateView, SedeDeleteView
from adminFCT.views import ContratoListView, ContratoDetailView, ContratoCreateView, ContratoUpdateView, ContratoDeleteView
from adminFCT.views import MedioListView, MedioCreateView, MedioUpdateView, MedioDeleteView
from adminFCT.views import MensajeListView, MensajeDetailView, MensajeCreateView, MensajeUpdateView, MensajeDeleteView
from adminFCT.views import PracticaListView, PracticaDetailView, PracticaCreateView, PracticaUpdateView, PracticaDeleteView

from adminFCT.views import ProfesorSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    #url para accounts
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    #url para alumno
    path('alumno/', AlumnoListView.as_view(), name='alumno-list'),
    path('alumno/<int:pk>',AlumnoDetailView.as_view(), name='alumno-detail'),

    #url para Forma
    path('forma/', FormaListView.as_view(), name='forma-list'),
    path('forma/add', FormaCreateView.as_view(), name='forma-add'),
    path('forma/<int:pk>/update', FormaUpdateView.as_view(), name='forma-update'),
    path('forma/<int:pk>/delete', FormaDeleteView.as_view(), name='forma-delete'),

    #url para Ramo
    path('ramo/', RamoListView.as_view(), name='ramo-list'),
    path('ramo/add', RamoCrateView.as_view(), name='ramo-add'),
    path('ramo/<int:pk>/update', RamoUpdateView.as_view(), name='ramo-update'),
    path('ramo/<int:pk>/delete', RamoDeleteView.as_view(), name='ramo-delete'),

    #url para Tamano
    path('tamano/', TamanoListView.as_view(), name='tamano-list'),
    path('tamano/add', TamanoCreateView.as_view(), name='tamano-add'),
    path('tamano/<int:pk>/update', TamanoUpdateView.as_view(), name='tamano-update'),
    path('tamano/<int:pk>/delete', TamanoDeleteView.as_view(), name='tamano-delete'),

    #url para empresa
    path('empresa/', EmpresaListView.as_view(), name='empresa-list'),
    path('empresa/<int:pk>', EmpresaDetailView.as_view(), name='empresa-detail'),
    path('empresa/add', EmpresaCreateView.as_view(), name='empresa-add'),
    path('empresa/<int:pk>/update', EmpresaUpdateView.as_view(), name='empresa-update'),
    path('empresa/<int:pk>/delete', EmpresaDeleteView.as_view(), name='empresa-delete'),

    #url para ciclo
    path('ciclo/', CicloListView.as_view(), name='ciclo-list'),
    path('ciclo/add', CicloCreateView.as_view(), name='ciclo-add'),
    path('ciclo/<int:pk>/update', CicloUpdateView.as_view(), name='ciclo-update'),
    path('ciclo/<int:pk>/delete', CicloDeleteView.as_view(), name='ciclo-delete'),

    #url para trayecto
    path('trayecto/', TrayectoListView.as_view(), name='trayecto-list'),
    path('trayecto/<int:pk>', TrayectoDetailView.as_view(), name='trayecto-detail'),
    path('trayecto/add', TrayectoCreateView.as_view(), name='trayecto-add'),
    path('trayecto/<int:pk>/update', TrayectoUpdateView.as_view(), name='trayecto-update'),
    path('trayecto/<int:pk>/delete', TrayectoDeleteView.as_view(), name='trayecto-delete'),

    #url para sede
    path('sede/', SedeListView.as_view(), name='sede-list'),
    path('sede/<int:pk>', SedeDetailView.as_view(), name='sede-detail'),
    path('sede/add', SedeCreateView.as_view(), name='sede-add'),
    path('sede/<int:pk>/update', SedeUpdateView.as_view(), name='sede-update'),
    path('sede/<int:pk>/delete', SedeDeleteView.as_view(), name='sede-delete'),

    #url para contactos
    path('contactos/<int:pk>', ContactosDetailView.as_view(), name='contactos-detail'),
    path('contactos/add', ContactosCreateView.as_view(), name='contactos-add'),
    path('contactos/<int:pk>/update', ContactosUpdateView.as_view(), name='contactos-update'),
    path('contactos/<int:pk>/delete', ContactosdeleteView.as_view(), name='contactos-delete'),

    #url para contrato
    path('contrato/', ContratoListView.as_view(), name='contrato-list'),
    path('contrato/<int:pk>', ContratoDetailView.as_view(), name='contrato-detail'),
    path('contrato/add', ContratoCreateView.as_view(), name='contrato-add'),
    path('contrato/<int:pk>/update', ContratoUpdateView.as_view(), name='contrato-update'),
    path('contrato/<int:pk>/detele', ContratoDeleteView.as_view(), name='contrato-delete'),

    #url para Medio
    path('medio/', MedioListView.as_view(), name='medio-list'),
    path('medio/add', MedioCreateView.as_view(), name='medio-add'),
    path('medio/<int:pk>/update', MedioUpdateView.as_view(), name='medio-update'),
    path('medio/<int:pk>/delete', MedioDeleteView.as_view(), name='medio-delete'),

    #url para mensaje
    path('mensaje/', MensajeListView.as_view(), name='mensaje-list'),
    path('mensaje/<int:pk>', MensajeDetailView.as_view(), name='mensaje-detail'),
    path('mensaje/add', MensajeCreateView.as_view(), name='mensaje-add'),
    path('mensaje/<int:pk>/update', MensajeUpdateView.as_view(), name='mensaje-update'),
    path('mensaje/<int:pk>/delete', MensajeDeleteView.as_view(), name='mensaje-delete'),

    #url para practica
    path('practica/', PracticaListView.as_view(), name='practica-list'),
    path('practica/<int:pk>', PracticaDetailView.as_view(), name='practica-detail'),
    path('practica/add', PracticaCreateView.as_view(), name='practica-add'),
    path('practica/<int:pk>/update', PracticaUpdateView.as_view(), name='practica-update'),
    path('practica/<int:pk>/delete', PracticaDeleteView.as_view(), name='practica-delete'),

    path('accounts/signup/teacher/', ProfesorSignUpView.as_view(), name='profesor_signup'),
]
