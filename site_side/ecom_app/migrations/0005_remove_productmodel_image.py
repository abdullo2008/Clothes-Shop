# Generated by Django 5.1.1 on 2024-12-09 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_delete_usermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
    ]
