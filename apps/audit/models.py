from django.db import models

from apps.common.models.base import TimeStampedModel


class AuditLog(TimeStampedModel):
    actor = models.ForeignKey('accounts.User', null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=120)
    entity_type = models.CharField(max_length=120)
    entity_id = models.CharField(max_length=64)
    metadata = models.JSONField(default=dict)
