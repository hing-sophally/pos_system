from django.db import models
from django.contrib.auth.models import User


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
    last_name = models.CharField(max_length=20, null=False, blank=False )
    first_name = models.CharField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=20, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='staff/', null=False, blank=False)


class Major(models.Model):
    SubjectName = models.CharField(max_length=20, unique=True)
    CreateAt = models.DateTimeField(auto_now_add=True)
    CreateBy = models.ForeignKey(User, related_name='majors_created', null=True, blank=True, on_delete=models.SET_NULL)
    UpdateAt = models.DateTimeField(auto_now=True)
    UpdateBy = models.ForeignKey(User, related_name='majors_updated', null=True, blank=True, on_delete=models.SET_NULL)

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dateOfBirth = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='teacher_photos/', null=True, blank=True)

    createAt = models.DateTimeField(auto_now_add=True)
    createBy = models.ForeignKey(
        User,
        related_name='teachers_created',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    updateAt = models.DateTimeField(auto_now=True)
    updateBy = models.ForeignKey(
        User,
        related_name='teachers_updated',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    major = models.ForeignKey(
        Major,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )