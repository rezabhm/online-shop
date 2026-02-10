from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PurchaseOrder
from .serializers import OrderSerializer
from .services import OrderService


class OrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.select_related('buyer', 'supplier', 'rfq').all()
    serializer_class = OrderSerializer
    filterset_fields = ['status', 'buyer', 'supplier']

    @action(detail=True, methods=['post'])
    def transition(self, request, pk=None):
        order = self.get_object()
        target_status = request.data.get('target_status')
        OrderService.transition(order, target_status)
        return Response(self.get_serializer(order).data)
