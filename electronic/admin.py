from django.contrib import admin
from .models import ElectronicItem, ElectronicItemImg, Electronic, laptop, MobilePhone, Tablet
# Register your models here.
admin.site.register(ElectronicItem)
admin.site.register(ElectronicItemImg)
admin.site.register(Electronic)
admin.site.register(laptop)
admin.site.register(MobilePhone)
admin.site.register(Tablet)
