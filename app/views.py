from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.forms import ContriForm
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


def contribuintes(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Contribuinte.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Contribuinte.objects.all()
    return render(request, 'contribuintes.html', data)

# Formulário usuário:


def form(request):
    data = {}
    data['form'] = ContriForm()
    return render(request, 'cadastrarContribuinte.html', data)


def cadastrarContribuinte(request):
    return render(request, 'cadastrarContribuinte.html')


def update_contribuinte(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    form = ContriForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('contribuinte')


# Create your views here.
def listarCarros(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()

    # all = Carros.objects.all()
    # paginator = Paginator(all, 2)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, 'listarCarros.html', data)


# Formulário pets:
def pets(request):
    return render(request, 'pets.html')


# Relatório de todos os cadastros:


def relatorio(request):
    return render(request, 'relatorio.html')

# Logout do sistema:


def logouts(request):
    logout(request)
    return redirect('/painel/')
