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
from adminFCT.views import EmpresaDeleteView, EmpresaDetailView, EmpresaListView, EmpresaCreateView, EmpresaUpdateView
from adminFCT.views import ContactosCreateView, ContactosdelteView, ContactosDetailView, ContactosUpdateView
from adminFCT.views import ProfesorSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    #url para accounts
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    #url para empresa
    path('empresa/', EmpresaListView.as_view(), name='empresa-list'),
    path('empresa/<int:pk>', EmpresaDetailView.as_view(), name='empresa-detail'),
    path('empresa/add', EmpresaCreateView.as_view(), name='empresa-add'),
    path('empresa/<int:pk>/update', EmpresaUpdateView.as_view(), name='empresa-update'),
    path('empresa/<int:pk>/delete', EmpresaDeleteView.as_view(), name='empresa-delete'),

    #url para contactos
    path('contactos/<int:pk>', ContactosDetailView.as_view(), name='contactos-detail'),
    path('contactos/add', ContactosCreateView.as_view(), name='contactos-add'),
    path('contactos/<int:pk>/update', ContactosUpdateView.as_view(), name='contactos-update'),
    path('contactos/<int:pk>/delete', ContactosdelteView.as_view(), name='contactos-delete'),

    path('accounts/signup/teacher/', ProfesorSignUpView.as_view(), name='profesor_signup'),
]
