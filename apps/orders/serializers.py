from rest_framework import serializers

from .models import PurchaseOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
