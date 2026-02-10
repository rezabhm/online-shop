from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.accounts.views import UserViewSet
from apps.catalog.views import ProductViewSet
from apps.marketplace.views import ListingViewSet
from apps.orders.views import OrderViewSet
from apps.payments.views import PaymentViewSet
from apps.rfq.views import RFQViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('products', ProductViewSet, basename='products')
router.register('listings', ListingViewSet, basename='listings')
router.register('rfqs', RFQViewSet, basename='rfqs')
router.register('orders', OrderViewSet, basename='orders')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.accounts.urls')),
    path('api/v1/', include(router.urls)),
]
