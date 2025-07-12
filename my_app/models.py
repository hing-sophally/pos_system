from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    barcode = models.BigIntegerField(null=False, blank=False, unique=True)
    sale_price = models.FloatField()
    unit_stock = models.IntegerField()
    photo = models.ImageField(upload_to='products/', null=False, blank=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Position(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)




class Staff(models.Model):
    last_name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    gender = models.CharField(max_length=20, null=False, blank=False, unique=True)
    date_of_birth = models.DateField(null=False, blank=False, unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='staff/', null=False, blank=False, unique=True)

