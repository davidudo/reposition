# Generated by Django 3.1.4 on 2021-01-19 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, default="/placeholder.png", null=True, upload_to=""
            ),
        ),
    ]
