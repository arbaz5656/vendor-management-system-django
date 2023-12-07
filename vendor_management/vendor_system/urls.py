from django.urls import path
from . import views
from .views import (
    VendorListCreateView,
    VendorRetrieveUpdateDestroyView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDestroyView,
    VendorPerformanceView,
    AcknowledgePurchaseOrderView,

)

urlpatterns = [
    path('',views.Home_page,name="Home page"),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(),
         name='acknowledge-purchase-order'),
]

