from django.db import models

from apps.common.models.base import TimeStampedModel


class RFQStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    OPEN = 'open', 'Open'
    NEGOTIATION = 'negotiation', 'Negotiation'
    AGREED = 'agreed', 'Agreed'
    CANCELLED = 'cancelled', 'Cancelled'


class RFQ(TimeStampedModel):
    buyer = models.ForeignKey('profiles.BuyerProfile', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    target_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=RFQStatus.choices, default=RFQStatus.DRAFT)


class RFQResponse(TimeStampedModel):
    rfq = models.ForeignKey(RFQ, on_delete=models.CASCADE, related_name='responses')
    supplier = models.ForeignKey('profiles.SupplierProfile', on_delete=models.CASCADE)
    quoted_price = models.DecimalField(max_digits=12, decimal_places=2)
    message = models.TextField()


class NegotiationMessage(TimeStampedModel):
    rfq = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    sender = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    content = models.TextField()
