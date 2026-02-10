from django.db import models

from apps.common.models.base import TimeStampedModel


class PaymentStatus(models.TextChoices):
    INITIATED = 'initiated', 'Initiated'
    ESCROW_HELD = 'escrow_held', 'Escrow Held'
    RELEASED = 'released', 'Released'
    REFUNDED = 'refunded', 'Refunded'
    FAILED = 'failed', 'Failed'


class Payment(TimeStampedModel):
    order = models.ForeignKey('orders.PurchaseOrder', on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.INITIATED)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3)
    transaction_reference = models.CharField(max_length=120, unique=True)


class Invoice(TimeStampedModel):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=80, unique=True)
    due_date = models.DateField()
