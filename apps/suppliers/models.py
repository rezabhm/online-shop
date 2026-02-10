from django.db import models

from apps.common.models.base import TimeStampedModel


class SupplierVerification(TimeStampedModel):
    supplier = models.OneToOneField('profiles.SupplierProfile', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    verified_by = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL)


class SupplierMetric(TimeStampedModel):
    supplier = models.ForeignKey('profiles.SupplierProfile', on_delete=models.CASCADE)
    on_time_delivery_score = models.DecimalField(max_digits=5, decimal_places=2)
    defect_rate = models.DecimalField(max_digits=5, decimal_places=2)
