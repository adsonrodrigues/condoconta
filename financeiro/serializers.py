from rest_framework import serializers
from financeiro.models import ContaBancaria, Extrato
from django.contrib.auth.models import User
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )
        

class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ContaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaBancaria
        fields = ('id', 'data', 'descricao', 'valor_transacao', 'numero_conta', 'saldo', 'tipo', 'titular')                  
        ordering = ('id',)

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['data', 'descricao', 'valor_transacao', 'saldo_conta']