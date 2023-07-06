from django.urls import path
from .views import CotizacionListView, CotizacionDetailView, CotizacionCreateView, CotizacionUpdateView, CotizacionDeleteView

urlpatterns = [
    path('', CotizacionListView.as_view(), name='cotizacion_list'),
    path('<int:pk>', CotizacionDetailView.as_view(), name='cotizacion_detail'),
    path('new', CotizacionCreateView.as_view(), name='cotizacion_new'),
    path('<int:pk>/edit', CotizacionUpdateView.as_view(), name='cotizacion_edit'),
    path('<int:pk>/delete', CotizacionDeleteView.as_view(),
         name='cotizacion_delete'),
]
