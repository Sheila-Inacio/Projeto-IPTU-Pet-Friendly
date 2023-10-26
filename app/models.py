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
