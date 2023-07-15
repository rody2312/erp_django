from django.db import models

class Proveedor(models.Model):
    AREAS_CHOICES = (
        ('agua', 'Agua'),
        ('mineria', 'Minería'),
        ('azucar', 'Azúcar'),
        ('gas', 'Gas'),
        ('Oil & gas UP', 'Oil & Gas UP'),
        ('Oil & gas DP', 'Oil & Gas DP'),
        ('eolica', 'Eólica'),
        ('solar', 'Solar'),
    )

    PAISES_CHOICES = (
        ('AR', 'Argentina'),
        ('BR', 'Brasil'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('MX', 'México'),
        ('PE', 'Perú'),
    )

    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=200)
    codigo_postal_proveedor = models.CharField(max_length=10)
    localidad_proveedor = models.CharField(max_length=100)
    pais_proveedor = models.CharField(max_length=100, choices=PAISES_CHOICES)
    telefono_proveedor = models.IntegerField()
    correo_proveedor = models.EmailField()
    area_proveedor = models.CharField(max_length=100, choices=AREAS_CHOICES)
    observaciones_proveedor = models.TextField()

    class Meta:
        db_table = 'proveedor'
