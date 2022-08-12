from django.db import models
from shoes.models import ShoesItem
from book.models import BookItem
from electronic.models import ElectronicItem
from user.models import User
# Create your models here.

class Order(models.Model):
    totalAmount = models.FloatField(default=0)
    status = models.CharField(default='', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Voucher(models.Model):
    name = models.CharField(max_length=255, default=0)
    discountPercent = models.FloatField(default=0)
    description = models.CharField(default='', max_length=255)
    order = models.OneToOneField(Order, models.SET_NULL, null=True, blank=True)


class Shipment(models.Model):
    type = models.CharField(max_length= 255, default='')
    cost = models.FloatField(default=0)
    address = models.CharField(max_length=255, default='')
    order = models.OneToOneField(Order, models.SET_NULL, null=True)


class Payment(models.Model):
    datePay = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(Order, models.SET_NULL, null=True)


class Credit(Payment):
    number = models.CharField(default='', max_length=255)
    type = models.CharField(default='', max_length=255)
    exDate = models.DateTimeField()


class Cash(Payment):
    cashier = models.CharField(max_length=255, default='')
    cashTendered = models.FloatField(default=0)


class Tranfer(Payment):
    name = models.CharField(max_length=255, default='')
    bankID = models.CharField(max_length=255, default='')


class Cart(models.Model):
    quantity = models.IntegerField(default=0)
    totalPrice = models.FloatField(default=0)
    shoesItem = models.ManyToManyField(ShoesItem)
    bookItem = models.ManyToManyField(BookItem)
    electronicItem = models.ManyToManyField(ElectronicItem)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)



