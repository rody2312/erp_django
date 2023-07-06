from django.urls import path
from .views import (
    OportunidadListView,
    OportunidadDetailView,
    OportunidadCreateView,
    OportunidadUpdateView,
    OportunidadDeleteView,
    index
)


urlpatterns = [
    # path('', index, name='index'),
    path('', OportunidadListView.as_view(), name='oportunidad_list'),
    path('<int:pk>/', OportunidadDetailView.as_view(), name='oportunidad_detail'),
    path('nueva/', OportunidadCreateView.as_view(), name='oportunidad_new'),
    path('<int:pk>/editar/', OportunidadUpdateView.as_view(),
         name='oportunidad_edit'),
    path('<int:pk>/eliminar/', OportunidadDeleteView.as_view(),
         name='oportunidad_delete'),

]
