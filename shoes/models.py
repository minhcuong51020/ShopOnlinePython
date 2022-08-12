from django.db import models

# Create your models here.
class Shoes(models.Model):
    name = models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=255, default='')
    countryOfOrigin = models.CharField(max_length=255, default='')
    material = models.CharField(max_length=255, default='')
    occasion = models.CharField(max_length=255, default='')
    fasteningType = models.CharField(max_length=255, default='')
    size = models.CharField(max_length=255, default='')
    heelsHeight = models.CharField(max_length=255, default='')
    wideFit = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class ShoesItem(models.Model):
    shoe = models.OneToOneField(Shoes, models.SET_NULL, null=True)
    price = models.FloatField(default=0)
    description = models.CharField(default='', max_length=255)
    header = models.CharField(max_length=255, default='')
    discount = models.FloatField(default=0)
    isPay = models.BooleanField(default=False)
    def __str__(self):
        return self.header

class ShoesItemImg(models.Model):
    shoesItem = models.ForeignKey(ShoesItem, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="shoes/")


class MenShoes(Shoes):
    leatherType = models.CharField(default='', max_length=255)


class WomanShoes(Shoes):
    session= models.CharField(max_length=255, default='')


class KidShoes(Shoes):
    gender = models.CharField(max_length=255, default='')
    recommendedAge = models.FloatField(default=0)
    shoesStyle = models.CharField(max_length=255, default='')

