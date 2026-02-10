from django.db import models

from apps.common.models.base import TimeStampedModel


class SupplierReview(TimeStampedModel):
    order = models.OneToOneField('orders.PurchaseOrder', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    quality_score = models.PositiveSmallIntegerField()
    communication_score = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
