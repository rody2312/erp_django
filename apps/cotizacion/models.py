from django.db import models

from apps.oportunidad.models import Oportunidad

class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    id_oportunidad = models.ForeignKey(Oportunidad, on_delete=models.CASCADE)
    id_incoterm = models.IntegerField()
    tipo_operacion = models.CharField(max_length=200)
    fecha_cotizacion = models.DateField()
    moneda = models.CharField(max_length=50)
    tipo_cambio = models.CharField(max_length=50)
    plazo_entrega = models.DateField()

    def __str__(self):
        return str(self.id_cotizacion)

    class Meta:
        db_table = 'cotizacion'
