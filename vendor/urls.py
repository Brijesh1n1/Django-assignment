from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register('vendors', VendorViewSet)
router.register('purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]