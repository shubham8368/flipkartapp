from django.db import models

# Create your models here.
# from datetime import datetime
from datetime import datetime


class Registration(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField()
    gender = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.email


class category(models.Model):
    name = models.CharField(max_length=50, null=True)
    images = models.ImageField(upload_to='upload/category/')

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_name = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    desc = models.TextField(max_length=400, null=True)
    pro_image = models.ImageField(upload_to='upload/product/')
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pro_name


class Order_details(models.Model):
    address = models.CharField(max_length=100, null=True)
    mobile = models.IntegerField()
    Quantity = models.IntegerField()
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Registration, on_delete=models.CASCADE)
    ststus = models.BooleanField(default=False)
    # date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.customer.first_name
