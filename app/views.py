from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,'home.html')

#Formulário de cadastro de usuários:
def create(request):
    return render(request,'create.html')


#Inserção dos dados dos usuários:
def store(request):
    data = {}
    if (request.POST ['password'] != request.POST['password-conf'] ):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
        
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso.'
        data['class'] = 'alert-success'
        
    return render(request,'create.html',data)

#Formulário do painel de login:

def painel(request):
    return render(request,'painel.html')


#Formulário do login:

def dologin(request):
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')   
    else:
        return render(request,'painel.html')
    
#Página inicial do dashboard

def dashboard(request):
    return render(request,'dashboard/home.html')

