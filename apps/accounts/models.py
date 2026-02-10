from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models.base import TimeStampedModel


class UserRole(models.TextChoices):
    BUYER = 'buyer', 'Buyer'
    SUPPLIER = 'supplier', 'Supplier'
    OPERATOR = 'operator', 'Operator'
    ADMIN = 'admin', 'Admin'


class VerificationStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    VERIFIED = 'verified', 'Verified'
    REJECTED = 'rejected', 'Rejected'


class User(AbstractUser, TimeStampedModel):
    role = models.CharField(max_length=20, choices=UserRole.choices)
    phone_number = models.CharField(max_length=20, blank=True)
    kyc_status = models.CharField(max_length=20, choices=VerificationStatus.choices, default=VerificationStatus.PENDING)

    class Meta:
        db_table = 'accounts_user'
