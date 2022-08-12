from django.contrib import admin
from .models import Order, Voucher, Shipment, Payment, Credit, Cash, Tranfer, Cart
# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Voucher)
admin.site.register(Shipment)
admin.site.register(Payment)
admin.site.register(Credit)
admin.site.register(Cash)
admin.site.register(Tranfer)
