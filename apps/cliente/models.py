from django.db import models


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    codigo_postal_cliente = models.CharField(max_length=10)
    localidad_cliente = models.CharField(max_length=100)
    pais_cliente = models.CharField(max_length=100)
    telefono_cliente = models.IntegerField()
    correo_cliente = models.EmailField()
    area_cliente = models.CharField(max_length=100)
    observaciones_cliente = models.TextField()

    class Meta:
        db_table = 'cliente'
