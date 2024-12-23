from rest_framework.viewsets import ModelViewSet

from utils.paginations import DefaultLimitOffSetPagination
from .serializers import CurrencyListSerializer, PurchasedCurrenciesListSerializer
from rest_framework.permissions import AllowAny
from .models import Currency, PurchasedCurrencies



class CurrencyModelViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencyListSerializer
    pagination_class = DefaultLimitOffSetPagination
    permission_classes = [AllowAny]


class PurchasedCurrenciesModelViewSet(ModelViewSet):
    queryset = PurchasedCurrencies.objects.all()
    serializer_class = PurchasedCurrenciesListSerializer
    pagination_class = DefaultLimitOffSetPagination
    permission_classes = [AllowAny]
