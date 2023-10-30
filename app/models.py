from django.db import models

# Cadastrar dados dos usuários:


class Contribuinte(models.Model):
    nome_completo = models.CharField(max_length=50)
    cpf = models.IntegerField()
    email = models.CharField(max_length=50)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    inscricao_municipal = models.IntegerField()
    indicacao_fiscal = models.IntegerField()

class Pets(models.Model):
    nome = models.CharField(max_length=150)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField()
    tamanho = models.CharField(max_length=100)
    contribuinte = models.IntegerField()
    numero_identificacao = models.IntegerField()
