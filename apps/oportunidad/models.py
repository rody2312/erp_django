from django.db import models

class Oportunidad(models.Model):
    id_oportunidad = models.AutoField(primary_key=True, db_column='id_oportunidad')
    id_gestion_comercial = models.IntegerField(db_column='id_gestion_comercial')
    id_cliente = models.IntegerField(db_column='id_cliente')
    id_contacto = models.IntegerField(db_column='id_contacto')
    id_proveedor = models.IntegerField(db_column='id_proveedor')
    id_area = models.IntegerField(db_column='id_area')
    alcance = models.CharField(max_length=200, db_column='alcance')
    fecha_inicio = models.DateField(db_column='fecha_inicio')
    fecha_termino = models.DateField(db_column='fecha_termino')
    monto_probable = models.IntegerField(db_column='monto_probable')
    fecha_facturacion = models.DateField(db_column='fecha_facturacion')
    probabilidad_a_oc = models.IntegerField(db_column='probabilidad_a_oc')
    observaciones = models.CharField(max_length=100, db_column='observaciones')

    class Meta:
        db_table = 'oportunidad'
