from django.core.exceptions import ValidationError

from apps.common.services.events import DomainEvent, emit

from .models import OrderStatus, PurchaseOrder

ORDER_ALLOWED_TRANSITIONS = {
    OrderStatus.CREATED: {OrderStatus.CONTRACT_SIGNED},
    OrderStatus.CONTRACT_SIGNED: {OrderStatus.DEPOSIT_PAID},
    OrderStatus.DEPOSIT_PAID: {OrderStatus.IN_PRODUCTION},
    OrderStatus.IN_PRODUCTION: {OrderStatus.QC_PASSED},
    OrderStatus.QC_PASSED: {OrderStatus.IN_TRANSIT},
    OrderStatus.IN_TRANSIT: {OrderStatus.CUSTOMS_CLEARANCE},
    OrderStatus.CUSTOMS_CLEARANCE: {OrderStatus.DELIVERED},
    OrderStatus.DELIVERED: {OrderStatus.CLOSED},
}


class OrderService:
    @staticmethod
    def transition(order: PurchaseOrder, target_status: str) -> PurchaseOrder:
        allowed = ORDER_ALLOWED_TRANSITIONS.get(order.status, set())
        if target_status not in allowed:
            raise ValidationError(f'invalid transition: {order.status} -> {target_status}')
        order.status = target_status
        order.save(update_fields=['status', 'updated_at'])
        emit(DomainEvent(name='order.status_changed', payload={'order_id': order.id, 'status': target_status}))
        return order
