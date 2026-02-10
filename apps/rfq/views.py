from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import RFQ
from .serializers import RFQSerializer
from .services import RFQService


class RFQViewSet(viewsets.ModelViewSet):
    queryset = RFQ.objects.select_related('buyer', 'product').all()
    serializer_class = RFQSerializer
    filterset_fields = ['status', 'buyer']

    @action(detail=True, methods=['post'])
    def open(self, request, pk=None):
        rfq = self.get_object()
        RFQService.open_rfq(rfq)
        return Response(self.get_serializer(rfq).data)
