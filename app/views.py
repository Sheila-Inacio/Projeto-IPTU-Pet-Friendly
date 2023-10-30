from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.forms import ContriForm
from app.forms import CarrosForm
from app.models import Contribuinte
from app.models import Carros

from django.contrib.auth import authenticate, login, logout


# Formulário de cadastro de usuários:
def create(request):
    return render(request, 'create.html')

# Inserção dos dados dos usuários:


def store(request):
    data = {}
    if (request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'

    else:
        user = User.objects.create_user(
            request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso.'
        data['class'] = 'alert-success'

    return render(request, 'create.html', data)

# Formulário do painel de login:


def painel(request):
    return render(request, 'painel.html')


# Formulário do login:
def dologin(request):
    data = {}
    user = authenticate(
        username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

# Após login:

# Página inicial do dashboard


def dashboard(request):
    return render(request, 'dashboard/home.html')

# Pagina usuário:




# PAGINA DE CONTRIBUINTES:

def contribuintes(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Contribuinte.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Contribuinte.objects.all()
    return render(request, 'contribuintes.html', data)

def cadastrarContribuinte(request):
    data = {}
    data['form'] = ContriForm()
    return render(request, 'cadastrarContribuinte.html', data)

def createContribuinte(request):
    form = ContriForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contribuintes/')
    
def viewContribuinte(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    return render(request, 'viewContribuinte.html', data)

def editContribuinte(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    data['form'] = ContriForm(instance=data['db'])
    return render(request, 'cadastrarContribuinte.html', data)

def updateContribuinte(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    form = ContriForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/contribuintes/')

def deleteContribuinte(request, pk):
    db = Contribuinte.objects.get(pk=pk)
    db.delete()
    return redirect('contribuintes')

# PAGINA DE PETS:
def listarCarros(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    return render(request, 'listarCarros.html', data)

def cadastrarCarros(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'cadastrarCarros.html', data)

def createCarros(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarCarros')

def viewCarros(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'viewContribuinte.html', data)

def editCarros(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'cadastrarCarros.html', data)

def updateCarros(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/listarCarros/')
    
def deleteCarros(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('listarCarros')

# Relatório de todos os cadastros:


def relatorio(request):
    return render(request, 'relatorio.html')

# Logout do sistema:


def logouts(request):
    logout(request)
    return redirect('/painel/')
