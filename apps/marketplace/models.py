from django.db import models

from apps.common.models.base import TimeStampedModel


class Listing(TimeStampedModel):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    lead_time_days = models.PositiveIntegerField(default=30)


class SavedSupplier(TimeStampedModel):
    buyer = models.ForeignKey('profiles.BuyerProfile', on_delete=models.CASCADE)
    supplier = models.ForeignKey('profiles.SupplierProfile', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('buyer', 'supplier')
