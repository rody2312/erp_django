from django.db import models


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=200)
    codigo_postal_proveedor = models.CharField(max_length=10)
    localidad_proveedor = models.CharField(max_length=100)
    pais_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.IntegerField()
    correo_proveedor = models.EmailField()
    area_proveedor = models.CharField(max_length=100)
    observaciones_proveedor = models.TextField()

    def __str__(self):
        return str(self.nombre_proveedor)
    
    class Meta:
        db_table = 'proveedor'
