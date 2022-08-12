from django.db import models

# Create your models here.
class Electronic(models.Model):
    productName = models.CharField(max_length=255, default='')
    batteryCapacity = models.CharField(max_length=255, default='')
    warrantyDuration = models.CharField(max_length=255, default='')
    warrantyType = models.CharField(max_length=255, default='')
    condition = models.CharField(max_length=255, default='')
    screenSize = models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.productName


class ElectronicItem(models.Model):
    electronic = models.OneToOneField(Electronic, models.SET_NULL, null=True)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=255, default='')
    header = models.CharField(max_length=255, default='')
    discount = models.FloatField(default=0)
    isPay = models.BooleanField(default=False)
    def __str__(self):
        return self.header


class ElectronicItemImg(models.Model):
    electronicItem = models.ForeignKey(ElectronicItem, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="electronic/")


class laptop(Electronic):
    ram = models.CharField(max_length=255, default='')
    laptopType = models.CharField(max_length=255, default='')
    storageType = models.CharField(max_length=255, default='')
    weight = models.CharField(max_length=255, default='')
    card = models.CharField(max_length=255, default='')

class MobilePhone(Electronic):
    ram = models.CharField(max_length=255, default='')
    processorType = models.CharField(max_length=255, default='')
    storageCapacity = models.CharField(max_length=255, default='')
    mobileCableType = models.CharField(max_length=255, default='')


class Tablet(Electronic):
    eReader = models.BooleanField(default=False)
    storageCapacity = models.CharField(max_length=255, default='')

