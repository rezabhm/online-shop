from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer
from .services import PaymentService


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('order').all()
    serializer_class = PaymentSerializer

    @action(detail=True, methods=['post'])
    def hold_escrow(self, request, pk=None):
        payment = self.get_object()
        PaymentService.hold_escrow(payment)
        return Response(self.get_serializer(payment).data)
