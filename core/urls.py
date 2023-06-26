from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oportunidad/', include('apps.oportunidad.urls')),
    path('cotizacion/', include('apps.cotizacion.urls')),
    path('venta/', include('apps.venta.urls')),
    path('cliente/', include('apps.cliente.urls')),
]
