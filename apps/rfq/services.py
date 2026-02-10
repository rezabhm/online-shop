from apps.common.services.events import DomainEvent, emit

from .models import RFQ, RFQStatus


class RFQService:
    @staticmethod
    def open_rfq(rfq: RFQ) -> RFQ:
        rfq.status = RFQStatus.OPEN
        rfq.save(update_fields=['status', 'updated_at'])
        emit(DomainEvent(name='rfq.opened', payload={'rfq_id': rfq.id}))
        return rfq
