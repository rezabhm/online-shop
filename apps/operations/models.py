from django.db import models

from apps.common.models.base import TimeStampedModel


class ProcurementTask(TimeStampedModel):
    order = models.ForeignKey('orders.PurchaseOrder', on_delete=models.CASCADE)
    assignee = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='open')


class InspectionReport(TimeStampedModel):
    order = models.ForeignKey('orders.PurchaseOrder', on_delete=models.CASCADE)
    inspector = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()
