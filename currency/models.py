import uuid
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_sale = models.PositiveIntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

class PurchasedCurrencies(models.Model):
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    currency_type = models.ForeignKey("Currency", on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.owner} | {self.count} | {self.currency_type}"
