# Generated by Django 4.2 on 2023-07-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0004_alter_cliente_area_cliente"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="observaciones_cliente",
            field=models.TextField(blank=True, null=True),
        ),
    ]