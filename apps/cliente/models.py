from django.db import models

class Cliente(models.Model):
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

    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    codigo_postal_cliente = models.CharField(max_length=10)
    localidad_cliente = models.CharField(max_length=100)
    PAISES_CHOICES = (
        ('AR', 'Argentina'),
        ('BR', 'Brasil'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('MX', 'México'),
        ('PE', 'Perú'),
    )
    pais_cliente = models.CharField(max_length=100, choices=PAISES_CHOICES)
    telefono_cliente = models.IntegerField()
    correo_cliente = models.EmailField()
    area_cliente = models.CharField(max_length=100, choices=AREAS_CHOICES)
    observaciones_cliente = models.TextField(blank=True, null=True)  # Campo opcional

    def __str__(self):
        return str(self.nombre_cliente)
    
    class Meta:
        db_table = 'cliente'
