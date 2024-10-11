from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserModel(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name
