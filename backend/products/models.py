from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    units = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name
