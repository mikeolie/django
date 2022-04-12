from asyncio import constants
import django
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Test(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=0)

def highlights_default():
    return list([''])


class Products(models.Model):
    date_added = models.DateTimeField(default=django.utils.timezone.now)
    on_hold_till = models.DateTimeField(default=django.utils.timezone.now)
    item_no = models.CharField(max_length=120)
    description = models.CharField(default="", max_length=256)
    total_units = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    avg_cogs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    margin = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    mintage = models.IntegerField(default=0)
    pop_known = models.CharField(default="", max_length=100)
    ngc_pop = models.IntegerField(default=0)
    pcgs_pop = models.IntegerField(default=0)
    total_pop = models.IntegerField(default=0)
    finer_known = models.IntegerField(default=0)
    highlights = ArrayField(models.CharField(max_length=256, blank=True), default=highlights_default)
    vendor = models.CharField(default="", max_length=256)
    categories = models.TextField(default="Peace")
    display_y_n = models.CharField(default="", max_length=256)
    images_y_n = models.CharField(default="", max_length=256)
