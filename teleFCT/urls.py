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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from adminFCT.views import AlumnoListView, AlumnoDetailView, AlumnoSearch
from adminFCT.views import ContactoListView, ContactoDetailView, ContactoCreateView, ContactoUpdateView, ContactodeleteView, ContactoUpdateView2, ContactoSearchNombre, ContactoSearchEmpresa
from adminFCT.views import FormaListView, FormaCreateView, FormaUpdateView, FormaDeleteView
from adminFCT.views import RamoListView, RamoCrateView, RamoUpdateView, RamoDeleteView
from adminFCT.views import TamanoListView, TamanoCreateView, TamanoUpdateView, TamanoDeleteView
from adminFCT.views import EmpresaDeleteView, EmpresaDetailView, EmpresaListView, EmpresaCreateView, EmpresaUpdateView, EmpresaSearch
from adminFCT.views import CicloListView, CicloCreateView, CicloUpdateView, CicloDeleteView
from adminFCT.views import TrayectoListView, TrayectoDetailView, TrayectoCreateView, TrayectoUpdateView, TrayectoDeleteView, TrayectoSearchAlumno, TrayectoSearchCiclo , TrayectoSearchPromocion
from adminFCT.views import SedeListView, SedeDetailView, SedeCreateView, SedeUpdateView, SedeDeleteView
from adminFCT.views import ContratoListView, ContratoDetailView, ContratoCreateView, ContratoAlumnoCreateView , ContratoUpdateView, ContratoDeleteView, ContratoSearchAlumno, ContratoSearchEmpresa
from adminFCT.views import MedioListView, MedioCreateView, MedioUpdateView, MedioDeleteView
from adminFCT.views import MensajeListView, MensajeDetailView, MensajeCreateView, MensajeRespuestaCreateView, MensajeUpdateView, MensajeDeleteView, MensajeSearch
from adminFCT.views import PracticaListView, PracticaDetailView, PracticaCreateView, PracticaUpdateView, PracticaDeleteView, PracticaSearchAlumno, PracticaSearchCiclo, PracticaSearchProfesor, PracticaSearchContacto
from adminFCT.views import ToolListView, ToolCreateView, ToolUpdateView, ToolDeleteView
from adminFCT.views import RequisitoListView, RequisitoCreateView, RequisitoUpdateView, RequisitoDeleteView
from adminFCT.views import PerfilListView, PerfilCreateView, PerfilUpdateView, PerfilDeleteView
from adminFCT.views import FuncionListView, FuncionCreateView, FuncionUpdateView, FuncionDeleteView
from adminFCT.views import OfertaListView, OfertaDetailView, OfertaCreateView, OfertaUpdateView, OfertaDeleteView, OfertaAlumnoCreateView, OfertaAlumnoListView
from adminFCT.views import OfertaSearchNombre, OfertaSearchEmpresa, OfertaSearchContacto, OfertaSearchRequisito, OfertaSearchPerfil, OfertaSearchFuncion

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', index, name='index'),

    #url para accounts
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    #url para alumno
    path('alumno/', AlumnoListView.as_view(), name='alumno-list'),
    path('alumno/<int:pk>',AlumnoDetailView.as_view(), name='alumno-detail'),
    path('alumno/search/', AlumnoSearch.as_view(), name='alumno-search'),

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
    path('empresa/search/', EmpresaSearch.as_view(), name='empresa-search'),

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
    path('trayecto/search/nombre', TrayectoSearchAlumno.as_view(), name='trayecto-search-alumno'),
    path('trayecto/search/ciclo', TrayectoSearchCiclo.as_view(), name='trayecto-search-ciclo'),
    path('trayecto/search/promo', TrayectoSearchPromocion.as_view(), name='trayecto-search-promo'),

    #url para sede
    path('sede/', SedeListView.as_view(), name='sede-list'),
    path('sede/<int:pk>', SedeDetailView.as_view(), name='sede-detail'),
    path('sede/add', SedeCreateView.as_view(), name='sede-add'),
    path('sede/<int:pk>/update', SedeUpdateView.as_view(), name='sede-update'),
    path('sede/<int:pk>/delete', SedeDeleteView.as_view(), name='sede-delete'),

    #url para contactos
    path('contacto/', ContactoListView.as_view(), name='contacto-list'),
    path('contacto/<int:pk>', ContactoDetailView.as_view(), name='contacto-detail'),
    path('contacto/add', ContactoCreateView.as_view(), name='contacto-add'),
    path('contacto/<int:pk>/update', ContactoUpdateView.as_view(), name='contacto-update'),
    path('contacto/<int:pk>/update2', ContactoUpdateView2.as_view(), name='contacto-update2'),
    path('contacto/<int:pk>/delete', ContactodeleteView.as_view(), name='contacto-delete'),
    path('contacto/search/nombre', ContactoSearchNombre.as_view(), name='contacto-search-nombre'),
    path('contacto/search/empresa', ContactoSearchEmpresa.as_view(), name='contacto-search-empresa'),

    #url para contrato
    path('contrato/', ContratoListView.as_view(), name='contrato-list'),
    path('contrato/<int:pk>', ContratoDetailView.as_view(), name='contrato-detail'),
    path('contrato/add', ContratoCreateView.as_view(), name='contrato-add'),
    path('contrato/add/alumno', ContratoAlumnoCreateView.as_view(), name='contrato-alumno-add'),
    path('contrato/<int:pk>/update', ContratoUpdateView.as_view(), name='contrato-update'),
    path('contrato/<int:pk>/detele', ContratoDeleteView.as_view(), name='contrato-delete'),
    path('contrato/search/alumno', ContratoSearchAlumno.as_view(), name='contrato-search-alumno'),
    path('contrato/search/empresa', ContratoSearchEmpresa.as_view(), name='contrato-search-empresa'),

    #url para Medio
    path('medio/', MedioListView.as_view(), name='medio-list'),
    path('medio/add', MedioCreateView.as_view(), name='medio-add'),
    path('medio/<int:pk>/update', MedioUpdateView.as_view(), name='medio-update'),
    path('medio/<int:pk>/delete', MedioDeleteView.as_view(), name='medio-delete'),

    #url para mensaje
    path('mensaje/', MensajeListView.as_view(), name='mensaje-list'),
    path('mensaje/<int:pk>', MensajeDetailView.as_view(), name='mensaje-detail'),
    path('mensaje/add', MensajeCreateView.as_view(), name='mensaje-add'),
    path('mensaje/<int:pk>/respuesta', MensajeRespuestaCreateView.as_view(), name='mensaje-respuesta'),
    path('mensaje/<int:pk>/update', MensajeUpdateView.as_view(), name='mensaje-update'),
    path('mensaje/<int:pk>/delete', MensajeDeleteView.as_view(), name='mensaje-delete'),
    path('mensaje/search/', MensajeSearch.as_view(), name='mensaje-search'),

    #url para practica
    path('practica/', PracticaListView.as_view(), name='practica-list'),
    path('practica/<int:pk>', PracticaDetailView.as_view(), name='practica-detail'),
    path('practica/add', PracticaCreateView.as_view(), name='practica-add'),
    path('practica/<int:pk>/update', PracticaUpdateView.as_view(), name='practica-update'),
    path('practica/<int:pk>/delete', PracticaDeleteView.as_view(), name='practica-delete'),
    path('practica/search/alumno', PracticaSearchAlumno.as_view(), name='practica-search-alumno'),
    path('practica/search/ciclo', PracticaSearchCiclo.as_view(), name='practica-search-ciclo'),
    path('practica/search/profesor', PracticaSearchProfesor.as_view(), name='practica-search-profesor'),
    path('practica/search/contacto', PracticaSearchContacto.as_view(), name='practica-search-contacto'),

    #url para tool
    path('tool/', ToolListView.as_view(), name='tool-list'),
    path('tool/add', ToolCreateView.as_view(), name='tool-add'),
    path('tool/<int:pk>/update', ToolUpdateView.as_view(), name='tool-update'),
    path('tool/<int:pk>/delete', ToolDeleteView.as_view(), name='tool-delete'),

    #url para requisito
    path('requisito/', RequisitoListView.as_view(), name='requisito-list'),
    path('requisito/add', RequisitoCreateView.as_view(), name='requisito-add'),
    path('requisito/<int:pk>/update', RequisitoUpdateView.as_view(), name='requisito-update'),
    path('requisito/<int:pk>/delete', RequisitoDeleteView.as_view(), name='requisito-delete'),

    #url para perfil
    path('perfil/', PerfilListView.as_view(), name='perfil-list'),
    path('perfil/add', PerfilCreateView.as_view(), name='perfil-add'),
    path('perfil/<int:pk>/update', PerfilUpdateView.as_view(), name='perfil-update'),
    path('perfil/<int:pk>/delete', PerfilDeleteView.as_view(), name='perfil-delete'),
    
    #url para funcion
    path('funcion/', FuncionListView.as_view(), name='funcion-list'),
    path('funcion/add', FuncionCreateView.as_view(), name='funcion-add'),
    path('funcion/<int:pk>/update', FuncionUpdateView.as_view(), name='funcion-update'),
    path('funcion/<int:pk>/delete', FuncionDeleteView.as_view(), name='funcion-delete'),

    #url para oferta
    path('', OfertaListView.as_view(), name='oferta-list'),
    path('oferta/alumno', OfertaAlumnoListView.as_view(), name='oferta-alumno-list'),
    path('oferta/<int:pk>/', OfertaDetailView.as_view(), name='oferta-detail'),
    path('oferta/add', OfertaCreateView.as_view(), name='oferta-add'),
    path('oferta/alu-add', OfertaAlumnoCreateView.as_view(), name='oferta-alumno-add'),
    path('oferta/<int:pk>/update', OfertaUpdateView.as_view(), name='oferta-update'),
    path('oferta/<int:pk>/delete', OfertaDeleteView.as_view(), name='oferta-delete'),
    path('oferta/search/nombre', OfertaSearchNombre.as_view(), name='oferta-search-nombre'),
    path('oferta/search/empresa', OfertaSearchEmpresa.as_view(), name='oferta-search-empresa'),
    path('oferta/search/contacto', OfertaSearchContacto.as_view(), name='oferta-search-contacto'),
    path('oferta/search/requisito', OfertaSearchRequisito.as_view(), name='oferta-search-requisito'),
    path('oferta/search/perfil', OfertaSearchPerfil.as_view(), name='oferta-search-perfil'),
    path('oferta/search/funcion', OfertaSearchFuncion.as_view(), name='oferta-search-funcion'),

    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)