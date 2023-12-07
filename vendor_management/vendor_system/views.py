from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.shortcuts import render,redirect
def Home_page(request):
    queryset = Vendor.objects.all()
    if request.GET.get('Search'):
        queryset = queryset.filter(name__icontains = request.GET.get('Search'))

    context={
        "veriable":queryset
    }
    return render(request,"Home.html",context)

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = HistoricalPerformanceSerializer


# vendor_system/views.py

from rest_framework import mixins
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class AcknowledgePurchaseOrderView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
