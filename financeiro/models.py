from django.db import models
from django.contrib.auth.models import User

class ContaBancaria(models.Model):
    
    TIPO_CONTA_CHOICES = (
        ('Poupanca', 'Poupança'),
        ('Corrente', 'Corrente'),
    )
    
    data = models.DateTimeField()
    descricao = models.CharField(max_length=255)
    valor_transacao = models.DecimalField(max_digits=10, decimal_places=2)
    numero_conta = models.CharField(max_length=10, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    titular = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CONTA_CHOICES)

    def __str__(self):
        return self.numero_conta
    

class Extrato(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=255)
    valor_transacao = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_conta = models.DecimalField(max_digits=10, decimal_places=2)
    conta = models.ForeignKey('ContaBancaria', on_delete=models.CASCADE)

    def __str__(self):
        return f'Extrato {self.id} - Conta {self.conta.numero_conta}'