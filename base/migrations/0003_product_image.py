# Generated by Django 3.1.4 on 2020-12-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_order_orderitem_review_shippingaddress"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
