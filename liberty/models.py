from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()


class Products(models.Model):
    date_added = models.DateTimeField()
    on_hold_till = models.DateTimeField()
    item_no = models.CharField(max_length=120)
    description = models.CharField(max_length=256)
