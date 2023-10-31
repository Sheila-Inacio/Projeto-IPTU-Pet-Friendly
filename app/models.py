from django.db import models

# Cadastrar dados dos usuários:


class Contribuinte(models.Model):
    nome_completo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    inscricao_municipal = models.CharField(max_length=50)
    indicacao_fiscal = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome_completo + ' - ' + self.inscricao_municipal

class Pets(models.Model):
    nome = models.CharField(max_length=150)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField()
    tamanho = models.CharField(max_length=100)
    contribuinte = models.ForeignKey('Contribuinte', on_delete=models.CASCADE)
    numero_identificacao = models.CharField(max_length=50)
