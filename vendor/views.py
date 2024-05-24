from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.db.models import Avg, F, Q
from django.utils.timezone import now

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        self.calculate_vendor_metrics(serializer.instance.vendor)

    def perform_create(self, serializer):
        super().perform_create(serializer)
        self.calculate_vendor_metrics(serializer.instance.vendor)

    def calculate_vendor_metrics(self, vendor):
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_orders = PurchaseOrder.objects.filter(vendor=vendor)
        
        # On-Time Delivery Rate
        on_time_deliveries = completed_orders.filter(delivery_date__lte=F('order_date')).count()
        vendor.on_time_delivery_rate = (on_time_deliveries / completed_orders.count()) * 100 if completed_orders.count() else 0

        # Quality Rating Average
        vendor.quality_rating_avg = completed_orders.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

        # Average Response Time
        response_times = completed_orders.exclude(acknowledgment_date__isnull=True).annotate(
            response_time=F('acknowledgment_date') - F('issue_date')
        ).aggregate(avg_response_time=Avg('response_time'))['avg_response_time']
        vendor.average_response_time = response_times.total_seconds() / 3600 if response_times else 0

        # Fulfillment
        fulfilled_orders = total_orders.filter(status='completed').count()
        vendor.fulfillment_rate = (fulfilled_orders / total_orders.count()) * 100 if total_orders.count() else 0

        vendor.save()

