# vendor_system/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    # Implement logic to update vendor metrics based on PurchaseOrder changes
    pass
