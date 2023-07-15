from django.db import models


class Oportunidad(models.Model):
    AREA_CHOICES = [
        ('agua', 'Agua'),
        ('mineria', 'Minería'),
        ('azucar', 'Azúcar'),
        ('gas', 'Gas'),
        ('Oil & gas UP', 'Oil & Gas UP'),
        ('Oil & gas DP', 'Oil & Gas DP'),
        ('eolica', 'Eólica'),
        ('solar', 'Solar'),
    ]
    PROBABILIDAD_OC_CHOICES = [
        (10, '10'),
        (25, '25'),
        (50, '50'),
        (75, '75'),
        (90, '90'),
    ]
    id_oportunidad = models.AutoField(primary_key=True)
    id_gestion_comercial = models.IntegerField()
    nombre_cliente = models.CharField(max_length=100, default='')
    nombre_contacto = models.CharField(max_length=100, default='')
    nombre_proveedor = models.CharField(max_length=100, default='')
    area = models.CharField(max_length=100, choices=AREA_CHOICES, default='')
    alcance = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    monto_probable = models.IntegerField()
    fecha_facturacion = models.DateField()
    probabilidad_a_oc = models.IntegerField(choices=PROBABILIDAD_OC_CHOICES)
    observaciones = models.CharField(max_length=100)

    class Meta:
        db_table = 'oportunidad'
