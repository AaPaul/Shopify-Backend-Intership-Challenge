from operator import mod
from django.db import models

# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField(null=False, blank=False)

    # def __str__(self) -> str:
    #     return self.name
    
        


class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.RESTRICT, null=False, blank=False)


