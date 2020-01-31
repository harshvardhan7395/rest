from django.contrib import admin

from resto.models import Rest
from resto.models import Items
from resto.models import Order
from resto.models import OrderItems

admin.site.register(Rest)
admin.site.register(Items)
admin.site.register(OrderItems)
admin.site.register(Order)

# Register your models here.
