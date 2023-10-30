from django.db import models

# Cadastrar dados dos usuários:


class Contribuinte(models.Model):
    nome_completo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    inscricao_municipal = models.CharField(max_length=50)
    indicacao_fiscal = models.CharField(max_length=50)


class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()


class Pets(models.Model):
    nome = models.CharField(max_length=150)
    raca = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    tamanho = models.IntegerField(max_length=100)
    contribuinte = models.IntegerField(max_length=100)
    numero_identificacao = models.IntegerField(max_length=100)
