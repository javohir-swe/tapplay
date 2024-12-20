from django.contrib import admin
from .models import Currency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "total_sale",
        "uuid",
        "id",
    ]
