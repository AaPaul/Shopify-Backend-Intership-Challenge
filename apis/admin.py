from django.contrib import admin

# Register your models here.
from .models import Inventory, Warehouse

admin.site.register(Inventory)
admin.site.register(Warehouse)