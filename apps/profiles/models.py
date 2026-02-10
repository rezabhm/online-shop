from django.conf import settings
from django.db import models

from apps.common.models.base import TimeStampedModel


class CompanyProfile(TimeStampedModel):
    legal_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=80, unique=True)


class BuyerProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.PROTECT)
    preferred_incoterm = models.CharField(max_length=20, blank=True)


class SupplierProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.PROTECT)
    factory_location = models.CharField(max_length=255)
    capacity_per_month = models.PositiveIntegerField(default=0)


class CompanyDocument(TimeStampedModel):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    file_url = models.URLField()
    is_verified = models.BooleanField(default=False)
