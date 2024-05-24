from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(blank=True, null=True)
    quality_rating_avg = models.FloatField(blank=True, null=True)
    average_response_time = models.FloatField(blank=True, null=True)
    fulfillment_rate = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    PO_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=PO_STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    on_time_delivery_rate = models.FloatField(blank=True, null=True)
    quality_rating_avg = models.FloatField(blank=True, null=True)
    average_response_time = models.FloatField(blank=True, null=True)
    fulfillment_rate = models.FloatField(blank=True, null=True)

