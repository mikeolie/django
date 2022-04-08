from cgi import print_exception
from email import message_from_string
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()


class Products(models.Model):
    date_added = models.DateTimeField()
    on_hold_till = models.DateTimeField()
    item_no = models.CharField(max_length=120)
    description = models.CharField(max_length=256)
    total_units = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    avg_cogs = models.DecimalField(max_digits=10, decimal_places=2,)
    profit = models.DecimalField(max_digits=10, decimal_places=2,)
    margin = models.DecimalField(max_digits=10, decimal_places=2,)
    mintage = models.IntegerField()
    pop_known = models.CharField(max_length=100)
    ngc_pop = models.IntegerField()
    pcgs_pop = models.IntegerField()
    total_pop = models.IntegerField()
    finer_known = models.IntegerField()
    highlights = models.TextField()
    vendor = models.CharField(max_length=256)
    categories = models.TextField()
    display_y_n = models.CharField(max_length=256)
    images_y_n = models.CharField(max_length=256)
