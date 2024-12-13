from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/clothes')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
