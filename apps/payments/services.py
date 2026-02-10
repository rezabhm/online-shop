from apps.common.services.events import DomainEvent, emit

from .models import Payment, PaymentStatus


class PaymentService:
    @staticmethod
    def hold_escrow(payment: Payment) -> Payment:
        payment.status = PaymentStatus.ESCROW_HELD
        payment.save(update_fields=['status', 'updated_at'])
        emit(DomainEvent(name='payment.escrow_held', payload={'payment_id': payment.id}))
        return payment
