from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.forms import ContriForm
from app.forms import PetsForm
from app.models import Contribuinte
from app.models import Pets
from django.db.models import Count


from django.contrib.auth import authenticate, login, logout


# Formulário de cadastro de usuários:
def create(request):
    return render(request, 'create.html')


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
        data['db'] = Contribuinte.objects.filter(
            nome_completo__icontains=search)
    else:
        data['db'] = Contribuinte.objects.all()
    return render(request, 'contribuintes.html', data)

# Formulário usuário:


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


# Cadastro dos pets:

def pets(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Pets.objects.filter(nome__icontains=search)
    else:
        data['db'] = Pets.objects.all()
    return render(request, 'pets.html', data)


def cadastrarPets(request):
    data = {}
    data['form'] = PetsForm()
    return render(request, 'cadastrarPets.html', data)


def createPets(request):
    form = PetsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/pets/')


def viewPets(request, pk):
    data = {}
    data['db'] = Pets.objects.get(pk=pk)
    return render(request, 'viewPets.html', data)


def editPets(request, pk):
    data = {}
    data['db'] = Pets.objects.get(pk=pk)
    data['form'] = PetsForm(instance=data['db'])
    return render(request, 'cadastrarPets.html', data)


def updatePets(request, pk):
    data = {}
    data['db'] = Pets.objects.get(pk=pk)
    form = PetsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/pets/')


def deletePets(request, pk):
    db = Pets.objects.get(pk=pk)
    db.delete()
    return redirect('pets')


# Relatório de todos os cadastros:


def relatorio(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Contribuinte.objects.filter(nome_completo__icontains=search).annotate(
            num_pets=Count('pets')).annotate(valor_pets=Count('pets')*50)
    else:
        data['db'] = Contribuinte.objects.annotate(
            num_pets=Count('pets')).annotate(valor_pets=Count('pets')*50)
    return render(request, 'relatorio.html', data)


def viewRelatorio(request, pk):
    data = {}
    data['db'] = Contribuinte.objects.get(pk=pk)
    data['pets'] = Pets.objects.filter(contribuinte__exact=pk)
    return render(request, 'viewRelatorio.html', data)

# Logout do sistema:


def logouts(request):
    logout(request)
    return redirect('/painel/')
