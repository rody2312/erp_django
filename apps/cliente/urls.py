from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('<int:pk>', ClienteDetailView.as_view(), name='cliente_detail'),
    path('new', ClienteCreateView.as_view(), name='cliente_new'),
    path('<int:pk>/edit', ClienteUpdateView.as_view(), name='cliente_edit'),
    path('<int:pk>/delete', ClienteDeleteView.as_view(), name='cliente_delete'),
]
