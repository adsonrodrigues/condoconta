from rest_framework import routers
from .views import ContaBancariaViewset, ConsultarExtratoAPIView, TransferenciaContaBancariaAPIView, UserViewset, ConsultarSaldoAPIView
from django.urls import path

router = routers.SimpleRouter()

router.register(r'contas', ContaBancariaViewset)
router.register(r'usuarios', UserViewset, basename='UserModel')

urlpatterns = [
    path('extrato/<str:numero_conta>/', ConsultarExtratoAPIView.as_view(), name='consultar_extrato'),
    path('transferencia/', TransferenciaContaBancariaAPIView.as_view(), name='transferencia_investimento'),
    path('saldo/<str:numero_conta>/', ConsultarSaldoAPIView.as_view(), name='consultar_saldo'),
]

urlpatterns += router.urls