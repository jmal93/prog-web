from django.db import models


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Insira o nome')
    idade = models.IntegerField(help_text='Insira a idade')
    salario = models.DecimalField(
        help_text='Insira o sálario', decimal_places=2, max_digits=6)
    email = models.EmailField(help_text='Insira o email', max_length=254)
    telefone = models.CharField(
        help_text='Insira o número de telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(
        help_text='Data de nascimento no formato DD/MM/AAAA',
        verbose_name='Data de nascimento')

    def __str__(self):
        return self.nome
