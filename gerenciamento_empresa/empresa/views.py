from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Projeto, Trainee, Meta, Membro, DiretorSetor
from .forms import MetaForm

def cadastro_projeto(request):
    # Implemente a lógica para cadastrar projetos
    return render(request, 'cadastro_projeto.html')

def cadastro_trainee(request):
    # Implemente a lógica para cadastrar trainees
    return render(request, 'cadastro_trainee.html')

def cadastro_meta(request):
    if request.method == 'POST':
        form = MetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redireciona para o dashboard após o cadastro
    else:
        form = MetaForm()
    return render(request, 'cadastro_meta.html', {'form': form})

def cadastro_membro(request):
    # Implemente a lógica para cadastrar membros
    return render(request, 'cadastro_membro.html')

def reset_senha(request):
    return render(request, 'reset_senha.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redireciona para o dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    return render(request, 'empresa/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crie um perfil de DiretorSetor se necessário
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro_usuario.html', {'form': form})

def dashboard(request):
    # Implemente a lógica para o dashboard do diretor de setor
    return render(request, 'dashboard.html')

def projetos(request):
    # Lógica para buscar os projetos em andamento
    projetos = ...
    return render(request, 'dashboard.html', {'projetos': projetos})

def setores(request):
    # Lógica para buscar os dados dos setores
    setores = ...
    return render(request, 'dashboard.html', {'setores': setores})

def metas(request):
    # Lógica para buscar os dados das metas
    metas = ...
    return render(request, 'dashboard.html', {'metas': metas})

def funcionarios(request):
    # Lógica para buscar os dados dos funcionários
    funcionarios = ...
    return render(request, 'dashboard.html', {'funcionarios': funcionarios})