from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.forms import ContriForm
from app.models import Contribuinte

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
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

# Página inicial do dashboard


def dashboard(request):
    return render(request, 'dashboard/home.html')

# Logout do sistema:


def logouts(request):
    logout(request)
    return redirect('/painel/')

# Alterar a senha:


def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password()
    user.save()
    logout(request)
    return redirect('/painel/')

# Pagina usuário:


def usuario(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Contribuinte.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Contribuinte.objects.all()
    return render(request, 'usuario.html', data)

# Formulário usuário:


def forms_usuario(request):
    return render(request, 'forms_usuario.html')


def form(request):
    data = {}
    data['form'] = ContriForm()
    return render(request, 'form.html', data)


def cadastrar_contribuinte(request):
    form = ContriForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('dashboard')


def view(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    data['form'] = ContriForm(instance=data['db'])
    return render(request, 'form.html', data)


def update_contribuinte(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    form = ContriForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('dashboard')


def delete(request, pk):
    db = Contribuinte.objects.get(pk=pk)
    db.delete()
    return redirect('dashboard')


# Formulário pets:
def pets(request):
    return render(request, 'pets.html')

# Relatório de todos os cadastros:


def relatorio(request):
    return render(request, 'relatorio.html')
