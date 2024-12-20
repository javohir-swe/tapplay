import uuid
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_sale = models.PositiveIntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

