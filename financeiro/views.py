from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from .models import ContaBancaria, Extrato
from rest_framework.decorators import api_view
from .serializers import ContaBancariaSerializer, UserSerializer, UserSerializerPost, ExtratoSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from datetime import datetime, date
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Extrato

   



class UserViewset(mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializerPost
        else:
            return UserSerializer
        
    def get_queryset(self):
        queryset = User.objects.all()
                
        return queryset


class ContaBancariaViewset(mixins.ListModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = ContaBancaria.objects.all()
    serializer_class = ContaBancariaSerializer
    

class ConsultarSaldoAPIView(APIView):
    def get(self, request, numero_conta):
        try:
            conta = ContaBancaria.objects.get(numero_conta=numero_conta)
            saldo = conta.saldo
            return Response({'saldo': saldo}, status=status.HTTP_200_OK)
        except ContaBancaria.DoesNotExist:
            return Response({'message': 'Conta não encontrada.'}, status=status.HTTP_404_NOT_FOUND)



class ConsultarExtratoAPIView(APIView):
    
    def get(self, request, numero_conta):
        data_atual = timezone.now()
        mes_atual = data_atual.month
        extratos_mes_atual = Extrato.objects.filter(data__month=mes_atual)
        
        serializer = ExtratoSerializer(extratos_mes_atual, many=True)

        return Response(serializer.data)


class TransferenciaContaBancariaAPIView(APIView):
    def post(self, request):
        numero_conta_origem = request.data.get('numero_conta_origem')
        numero_conta_destino = request.data.get('numero_conta_destino')
        valor_transferencia = Decimal(request.data.get('valor_transferencia'))

        conta_origem = get_object_or_404(ContaBancaria, numero_conta=numero_conta_origem)
        conta_destino = get_object_or_404(ContaBancaria, numero_conta=numero_conta_destino)
        
        
        if numero_conta_origem == numero_conta_destino:
            return Response({'message': 'Não é possível realizar a transferência as contas possuem o mesmo Titular.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if conta_origem.titular != conta_destino.titular:
            return Response({'message': 'As contas não possuem o mesmo Titular.'}, status=status.HTTP_400_BAD_REQUEST)

        if conta_origem.saldo < valor_transferencia:
            return Response({'message': 'Você não possui saldo suficiente para realizar essa transação.'}, status=status.HTTP_400_BAD_REQUEST)
        

        conta_origem.saldo -= valor_transferencia
        conta_destino.saldo += valor_transferencia
        conta_origem.save()
        conta_destino.save()
        
        extrato_origem = Extrato.objects.create(
            data=datetime.now(),
            descricao=f'Transferência para conta {conta_destino}',
            valor_transacao=-valor_transferencia,
            saldo_conta=conta_origem.saldo,
            conta=conta_origem
        )

        extrato_destino = Extrato.objects.create(
            data=datetime.now(),
            descricao=f'Transferência da conta {conta_origem}',
            valor_transacao=valor_transferencia,
            saldo_conta=conta_destino.saldo,
            conta=conta_destino
        )
        
        extrato_origem.save()
        extrato_destino.save()

        return Response({'message': 'Transferência realizada com sucesso.'}, status=status.HTTP_200_OK)
