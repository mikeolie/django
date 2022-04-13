from cgi import print_exception
from email import message_from_string
from pyexpat import model
from django.db import models
from django_seed import Seed


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
    avg_cogs = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    margin = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    mintage = models.IntegerField()
    pop_known = models.CharField(max_length=100)
    ngc_pop = models.IntegerField()
    pcgs_pop = models.IntegerField()
    total_pop = models.IntegerField()
    finer_known = models.IntegerField()
    highlights = models.TextField()
    vendor = models.CharField(max_length=256)
    categories = models.TextField(default="Peace")
    display_y_n = models.CharField(max_length=256)
    images_y_n = models.CharField(max_length=256)


class RequestLog(models.Model):
    advisor = models.CharField(max_length=120)
    customer = models.IntegerField()
    description = models.CharField(max_length=120)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    grade = models.CharField(max_length=120)
    notes = models.TextField()
    admin_notes = models.TextField()
    status = models.CharField(max_length=120)
    sold = models.CharField(max_length=120)
    display_y_n = models.CharField(max_length=120)
    timestamp = models.DateTimeField()
