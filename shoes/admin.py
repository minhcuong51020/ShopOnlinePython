from django.contrib import admin
from .models import ShoesItem, ShoesItemImg, Shoes, MenShoes, WomanShoes, KidShoes

# Register your models here.
admin.site.register(Shoes)
admin.site.register(MenShoes)
admin.site.register(WomanShoes)
admin.site.register(KidShoes)
admin.site.register(ShoesItem)
admin.site.register(ShoesItemImg)