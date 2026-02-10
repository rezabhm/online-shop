from django.db import models

from apps.common.models.base import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


class Product(TimeStampedModel):
    supplier = models.ForeignKey('profiles.SupplierProfile', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField()
    moq = models.PositiveIntegerField()
    production_time_days = models.PositiveIntegerField()
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
