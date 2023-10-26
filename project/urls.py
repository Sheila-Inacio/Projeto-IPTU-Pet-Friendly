"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import painel, create, store, dologin, dashboard, logouts, changePassword, usuario, forms_usuario,cadastrar_contribuinte, pets, relatorio, view, edit, update_contribuinte, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', painel, name="painel"),
    path('create/', create, name="create"),
    path('store/', store, name="store"),
    path('dologin/', dologin, name="dologin"),
    path('painel/', painel, name="painel"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logouts/', logouts, name="logouts"),
    path('password/', changePassword, name="password"),
    path('usuario/', usuario, name="usuario"),
    path('forms_usuario/', forms_usuario, name="forms_usuario"),
    path('cadastrar_contribuinte/', cadastrar_contribuinte, name="cadastrar_contribuinte"),
    path('pets/', pets, name="pets"),
    path('relatorio/', relatorio, name="relatorio"),
    path('view/<int:pk>/', view, name="view"),
    path('edit/<int:pk>/', edit, name="edit"),
    path('update_contruibuinte/<int:pk>/', update_contribuinte, name="update_contribuinte"),
    path('delete/<int:pk>/', delete, name="delete"),
    
    
]
