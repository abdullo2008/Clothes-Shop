# Generated by Django 5.1.1 on 2024-12-09 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_alter_usermodel_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
