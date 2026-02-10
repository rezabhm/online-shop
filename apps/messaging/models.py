from django.db import models

from apps.common.models.base import TimeStampedModel


class Conversation(TimeStampedModel):
    order = models.ForeignKey('orders.PurchaseOrder', null=True, blank=True, on_delete=models.CASCADE)
    rfq = models.ForeignKey('rfq.RFQ', null=True, blank=True, on_delete=models.CASCADE)


class Message(TimeStampedModel):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    content = models.TextField()
    attachment_url = models.URLField(blank=True)
