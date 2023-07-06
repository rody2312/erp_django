from django.urls import path
from .views import VentaListView, VentaDetailView, VentaCreateView, VentaUpdateView, VentaDeleteView

urlpatterns = [
    path('', VentaListView.as_view(), name='venta_list'),
    path('<int:pk>', VentaDetailView.as_view(), name='venta_detail'),
    path('new', VentaCreateView.as_view(), name='venta_new'),
    path('<int:pk>/edit', VentaUpdateView.as_view(), name='venta_edit'),
    path('<int:pk>/delete', VentaDeleteView.as_view(), name='venta_delete'),
]
