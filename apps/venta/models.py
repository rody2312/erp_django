from django.db import models
from apps.oportunidad.models import Oportunidad
from apps.cotizacion.models import Cotizacion

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    n_orden_compra = models.IntegerField()
    fecha_orden_compra = models.DateField()
    
    MONEDA_CHOICES = Cotizacion.MONEDA_CHOICES
    moneda = models.CharField(max_length=50, choices=MONEDA_CHOICES)
    
    # tipo_cambio es definido como FloatField
    tipo_cambio = models.FloatField()
    
    fecha_entrega_oc = models.DateField()
    fecha_facturacion = models.DateField()
    utilidad_esperada = models.FloatField()
    observaciones = models.TextField(blank=True, null=True)  # Campo opcional

    def __str__(self):
        return str(self.id_venta)

    class Meta:
        db_table = 'venta'
