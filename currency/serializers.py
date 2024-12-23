from rest_framework import serializers

from .models import Currency, PurchasedCurrencies


class CurrencyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = "__all__"


class PurchasedCurrenciesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedCurrencies
        fields = "__all__"
