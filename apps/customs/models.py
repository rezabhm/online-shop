from django.db import models

from apps.common.models.base import TimeStampedModel


class CustomsClearance(TimeStampedModel):
    shipment = models.OneToOneField('logistics.Shipment', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')
    tariff_amount = models.DecimalField(max_digits=12, decimal_places=2)


class ComplianceDocument(TimeStampedModel):
    clearance = models.ForeignKey(CustomsClearance, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=120)
    file_url = models.URLField()
