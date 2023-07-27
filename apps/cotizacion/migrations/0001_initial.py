# Generated by Django 4.2 on 2023-07-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("oportunidad", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cotizacion",
            fields=[
                ("id_cotizacion", models.AutoField(primary_key=True, serialize=False)),
                (
                    "incoterm",
                    models.CharField(
                        choices=[
                            ("EXW", "EXW"),
                            ("FOB", "FOB"),
                            ("DAP", "DAP"),
                            ("DAT", "DAT"),
                            ("CIP", "CIP"),
                            ("CIF", "CIF"),
                            ("FCA", "FCA"),
                            ("CPT", "CPT"),
                        ],
                        default="",
                        max_length=200,
                    ),
                ),
                (
                    "tipo_operacion",
                    models.CharField(
                        choices=[("EXW", "EXW"), ("NAC", "NAC"), ("SERV", "SERV")],
                        max_length=200,
                    ),
                ),
                (
                    "moneda",
                    models.CharField(
                        choices=[
                            ("EURO", "EURO"),
                            ("DOLAR", "DOLAR"),
                            ("PESO ARGENTINO", "PESO ARGENTINO"),
                            ("PESO COLOMBIANO", "PESO COLOMBIANO"),
                            ("PESO CHILENO", "PESO CHILENO"),
                            ("SOL PERUANO", "SOL PERUANO"),
                        ],
                        max_length=50,
                    ),
                ),
                ("tipo_cambio", models.FloatField()),
                ("plazo_entrega", models.DateField()),
                ("fecha_cotizacion", models.DateField()),
                (
                    "id_oportunidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oportunidad.oportunidad",
                    ),
                ),
            ],
            options={"db_table": "cotizacion",},
        ),
    ]
