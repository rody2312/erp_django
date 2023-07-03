# Generated by Django 4.2 on 2023-07-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oportunidad", "0002_remove_oportunidad_id_area_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oportunidad",
            name="area",
            field=models.CharField(
                choices=[
                    ("agua", "Agua"),
                    ("mineria", "Minería"),
                    ("azucar", "Azúcar"),
                    ("gas", "Gas"),
                    ("Oil & gas UP", "Oil & Gas UP"),
                    ("Oil & gas DP", "Oil & Gas DP"),
                    ("eolica", "Eólica"),
                    ("solar", "Solar"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
