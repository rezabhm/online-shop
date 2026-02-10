from django.db import models

from apps.common.models.base import TimeStampedModel


class Notification(TimeStampedModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    channel = models.CharField(max_length=20)
    event_name = models.CharField(max_length=120)
    payload = models.JSONField(default=dict)
    is_read = models.BooleanField(default=False)
