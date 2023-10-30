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
from app.views import painel, create, store, dologin, dashboard, logouts, contribuintes, cadastrarContribuinte, createContribuinte, viewContribuinte, editContribuinte, updateContribuinte, deleteContribuinte, listarCarros, cadastrarCarros, createCarros, viewCarros, editCarros, updateCarros, deleteCarros, pets, cadastrarPets, createPets, viewPets, editPets, updatePets, deletePets,  relatorio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', painel, name="painel"),
    path('create/', create, name="create"),
    path('store/', store, name="store"),
    path('dologin/', dologin, name="dologin"),
    path('painel/', painel, name="painel"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logouts/', logouts, name="logouts"),
    path('contribuintes/', contribuintes, name="contribuintes"),
    path('cadastrarContribuinte/', cadastrarContribuinte,
         name="cadastrarContribuinte"),
    path('createContribuinte/', createContribuinte, name="createContribuinte"),
    path('viewContribuinte/<int:pk>/', viewContribuinte, name='viewContribuinte'),
    path('editContribuinte/<int:pk>/', editContribuinte, name='editContribuinte'),
    path('updateContribuinte/<int:pk>/',
         updateContribuinte, name='updateContribuinte'),
    path('deleteContribuinte/<int:pk>/',
         deleteContribuinte, name='deleteContribuinte'),
    path('listarCarros/', listarCarros, name="listarCarros"),
    path('cadastrarCarros/', cadastrarCarros, name="cadastrarCarros"),
    path('createCarros/', createCarros, name="createCarros"),
    path('viewCarros/<int:pk>/', viewCarros, name='viewCarros'),
    path('editCarros/<int:pk>/', editCarros, name='editCarros'),
    path('updateCarros/<int:pk>/', updateCarros, name='updateCarros'),
    path('deleteCarros/<int:pk>/', deleteCarros, name='deleteCarros'),
    path('pets/', pets, name="pets"),
    path('cadastrarPets/', cadastrarPets, name="cadastrarPets"),
    path('createPets/', createPets, name="createPets"),
    path('viewPets/<int:pk>/', viewPets, name='viewPets'),
    path('editPets/<int:pk>/', editPets, name='editPets'),
    path('updatePets/<int:pk>/', updatePets, name='updatePets'),
    path('deletePets/<int:pk>/', deletePets, name='deletePets'),
    path('relatorio/', relatorio, name="relatorio"),




]
