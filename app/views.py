from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
    return render(request,'dashboard/home.html')

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
