# Generated by Django 5.1.1 on 2024-12-11 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0007_productmodel_added_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to='images/clothes'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
