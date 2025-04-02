from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    dias_uteis = models.IntegerField()
    coordenadores = models.ManyToManyField(User, related_name='projetos_coordenados')
    projetistas = models.ManyToManyField(User, related_name='projetos_projetados')

    def __str__(self):
        return self.nome

class Trainee(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    curso = models.CharField(max_length=100)
    semestre = models.IntegerField()

    def __str__(self):
        return self.nome

class Meta(models.Model):
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao

class Membro(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    area = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Adicione campos para o Dashboard
class DiretorSetor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    setor = models.CharField(max_length=100) # Ex: Vendas, Marketing, etc.

    def __str__(self):
        return self.usuario.username
    
class Meta(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    setor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome