from rest_framework import viewsets

from .models import Listing
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.select_related('product').all()
    serializer_class = ListingSerializer
    filterset_fields = ['is_active']
    search_fields = ['product__name']
