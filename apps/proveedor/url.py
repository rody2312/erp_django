from django.urls import path
from .views import (
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
)


urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor_list'),
    path('<int:pk>', ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('new', ProveedorCreateView.as_view(), name='proveedor_new'),
    path('<int:pk>/edit', ProveedorUpdateView.as_view(), name='proveedor_edit'),
    path('<int:pk>/delete', ProveedorDeleteView.as_view(), name='proveedor_delete'),
]
