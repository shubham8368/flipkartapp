# Generated by Django 4.1.3 on 2022-11-25 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("flipkart", "0002_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("pro_name", models.CharField(max_length=50, null=True)),
                ("price", models.IntegerField()),
                ("desc", models.TextField(max_length=400, null=True)),
                ("pro_image", models.ImageField(upload_to="upload/product/")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flipkart.category",
                    ),
                ),
            ],
        ),
    ]