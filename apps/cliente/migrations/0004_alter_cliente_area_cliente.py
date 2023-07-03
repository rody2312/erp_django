# Generated by Django 4.2 on 2023-07-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0003_alter_cliente_area_cliente"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="area_cliente",
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
                max_length=100,
            ),
        ),
    ]
