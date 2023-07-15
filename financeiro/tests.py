from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import ContaBancaria
from rest_framework import status
from decimal import Decimal

class TransferenciaInvestimentoAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='adson', password='testeteste')
        self.conta_corrente = ContaBancaria.objects.create(
            data='2023-07-15',
            descricao='teste',
            valor_transacao=100.00,
            numero_conta='456',
            saldo=1000.00,
            tipo='Corrente',
            titular=self.user
        )
        self.conta_poupanca = ContaBancaria.objects.create(
            data='2023-07-15',
            descricao='teste',
            valor_transacao=100.00,
            numero_conta='123',
            saldo=1.00,
            tipo='Poupanca',
            titular=self.user
        )

    def test_transferencia_investimento_sucesso(self):
        self.client.login(username='adson', password='testeteste')
        data = {
            'numero_conta_origem': 456,
            'numero_conta_destino': 123,
            'valor_transferencia': 50.00
        }
        response = self.client.post('/api/transferencia/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Transferência realizada com sucesso.')

        self.conta_corrente.refresh_from_db()
        self.conta_poupanca.refresh_from_db()
        self.assertEqual(self.conta_corrente.saldo, Decimal('950.00'))  
        self.assertEqual(self.conta_poupanca.saldo, Decimal('51.00'))

    def test_transferencia_resgate_sucesso(self):
        self.client.login(username='adson', password='testeteste')
        data = {
            'numero_conta_origem': 123,
            'numero_conta_destino': 456,
            'valor_transferencia': 1.00
        }
        response = self.client.post('/api/transferencia/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Transferência realizada com sucesso.')

        self.conta_corrente.refresh_from_db()
        self.conta_poupanca.refresh_from_db()
        self.assertEqual(self.conta_corrente.saldo, Decimal('1001.00'))
        self.assertEqual(self.conta_poupanca.saldo, Decimal('0.00'))
        
    def test_transferencia_investimento_falha(self):
        self.client.login(username='adson', password='testeteste')
        data = {
            'numero_conta_origem': 456,
            'numero_conta_destino': 123,
            'valor_transferencia': 5000.00
        }
        response = self.client.post('/api/transferencia/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Você não possui saldo suficiente para realizar essa transação.')

        self.conta_corrente.refresh_from_db()
        self.conta_poupanca.refresh_from_db()
        self.assertEqual(self.conta_corrente.saldo, Decimal('1000.00'))  
        self.assertEqual(self.conta_poupanca.saldo, Decimal('1.00'))

    def test_transferencia_resgate_falha(self):
        self.client.login(username='adson', password='testeteste')
        data = {
            'numero_conta_origem': 123,
            'numero_conta_destino': 123,
            'valor_transferencia': 10.00
        }
        response = self.client.post('/api/transferencia/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Não é possível realizar a transferência as contas possuem o mesmo Titular.')

        self.conta_corrente.refresh_from_db()
        self.conta_poupanca.refresh_from_db()
        self.assertEqual(self.conta_corrente.saldo, Decimal('1000.00'))
        self.assertEqual(self.conta_poupanca.saldo, Decimal('1.00'))
