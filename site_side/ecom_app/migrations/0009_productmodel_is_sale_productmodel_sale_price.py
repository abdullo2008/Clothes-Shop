# Generated by Django 5.1.1 on 2024-12-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0008_alter_productmodel_image_alter_productmodel_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
