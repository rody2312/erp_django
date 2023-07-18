from django.db import models
from apps.oportunidad.models import Oportunidad

class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    id_oportunidad = models.ForeignKey(Oportunidad, on_delete=models.CASCADE)
    
    INCOTERM_CHOICES = [
        ('EXW', 'EXW'),
        ('FOB', 'FOB'),
        ('DAP', 'DAP'),
        ('DAT', 'DAT'),
        ('CIP', 'CIP'),
        ('CIF', 'CIF'),
        ('FCA', 'FCA'),
        ('CPT', 'CPT'),
    ]
    incoterm = models.CharField(max_length=200, choices=INCOTERM_CHOICES, default='')
    
    TIPO_OPERACION_CHOICES = [
        ('EXW', 'EXW'),
        ('NAC', 'NAC'),
        ('SERV', 'SERV'),
    ]
    tipo_operacion = models.CharField(max_length=200, choices=TIPO_OPERACION_CHOICES)
    
    MONEDA_CHOICES = [
        ('EURO', 'EURO'),
        ('DOLAR', 'DOLAR'),
        ('PESO ARGENTINO', 'PESO ARGENTINO'),
        ('PESO COLOMBIANO', 'PESO COLOMBIANO'),
        ('PESO CHILENO', 'PESO CHILENO'),
        ('SOL PERUANO', 'SOL PERUANO'),
    ]
    moneda = models.CharField(max_length=50, choices=MONEDA_CHOICES)
    
    tipo_cambio = models.FloatField()
    plazo_entrega = models.DateField()
    
    # Agrega el campo fecha_cotizacion
    fecha_cotizacion = models.DateField()

    def __str__(self):
        return str(self.id_cotizacion)

    class Meta:
        db_table = 'cotizacion'
