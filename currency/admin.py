from django.contrib import admin
from .models import Currency, PurchasedCurrencies

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "total_sale",
        "uuid",
        "id",
    ]


@admin.register(PurchasedCurrencies)
class PurchasedCurrenciesAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "currency_type",
        "count",
        "id",
    ]
    list_filter = ["currency_type"]
