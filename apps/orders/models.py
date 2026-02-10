from django.db import models

from apps.common.models.base import TimeStampedModel


class OrderStatus(models.TextChoices):
    CREATED = 'created', 'Created'
    CONTRACT_SIGNED = 'contract_signed', 'Contract Signed'
    DEPOSIT_PAID = 'deposit_paid', 'Deposit Paid'
    IN_PRODUCTION = 'in_production', 'In Production'
    QC_PASSED = 'qc_passed', 'QC Passed'
    IN_TRANSIT = 'in_transit', 'In Transit'
    CUSTOMS_CLEARANCE = 'customs_clearance', 'Customs Clearance'
    DELIVERED = 'delivered', 'Delivered'
    CLOSED = 'closed', 'Closed'


class PurchaseOrder(TimeStampedModel):
    rfq = models.OneToOneField('rfq.RFQ', on_delete=models.PROTECT)
    buyer = models.ForeignKey('profiles.BuyerProfile', on_delete=models.PROTECT)
    supplier = models.ForeignKey('profiles.SupplierProfile', on_delete=models.PROTECT)
    status = models.CharField(max_length=30, choices=OrderStatus.choices, default=OrderStatus.CREATED)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')


class OrderMilestone(TimeStampedModel):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='milestones')
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
