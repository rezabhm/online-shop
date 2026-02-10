from django.db import models

from apps.common.models.base import TimeStampedModel


class Shipment(TimeStampedModel):
    order = models.OneToOneField('orders.PurchaseOrder', on_delete=models.CASCADE)
    carrier = models.CharField(max_length=120)
    tracking_number = models.CharField(max_length=120, unique=True)
    estimated_arrival = models.DateField(null=True, blank=True)


class WarehouseEntry(TimeStampedModel):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    warehouse_code = models.CharField(max_length=80)
    received_quantity = models.PositiveIntegerField()
