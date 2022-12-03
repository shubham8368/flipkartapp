# Generated by Django 4.1.3 on 2022-11-26 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("flipkart", "0003_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order_detl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=100, null=True)),
                ("mobile", models.IntegerField()),
                ("Quantity", models.IntegerField()),
                ("price", models.IntegerField()),
                ("ststus", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flipkart.registration",
                    ),
                ),
                (
                    "prouct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flipkart.product",
                    ),
                ),
            ],
        ),
    ]