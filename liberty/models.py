import django
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Test(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=0, blank=True)


def array_default():
    return list([''])


class Category(models.Model):
    name = models.CharField(default="", max_length=120)
    parent_category = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.DO_NOTHING)


class RequestLog(models.Model):
    advisor = models.CharField(default="", max_length=120)
    customer = models.IntegerField(default=0, blank=True)
    description = models.CharField(default="", max_length=120)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    grade = models.CharField(default="", max_length=120)
    notes = models.TextField(default="")
    admin_notes = models.TextField(default="")
    status = models.CharField(default="", max_length=120)
    sold = models.CharField(default="", max_length=120)
    display_y_n = models.CharField(default="", max_length=120)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)


class Products(models.Model):
    date_added = models.DateTimeField(default=django.utils.timezone.now)
    on_hold_till = models.DateTimeField(default=django.utils.timezone.now)
    item_no = models.CharField(max_length=120, default="")
    description = models.CharField(default="", max_length=256)
    total_units = models.IntegerField(default=0, blank=True)
    is_featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    avg_cogs = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    margin = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    mintage = models.IntegerField(default=0, blank=True)
    pop_known = models.CharField(default="", blank=True, max_length=100)
    ngc_pop = models.IntegerField(default=0, blank=True)
    pcgs_pop = models.IntegerField(default=0, blank=True)
    total_pop = models.IntegerField(default=0, blank=True)
    finer_known = models.IntegerField(default=0, blank=True)
    highlights = ArrayField(models.CharField(
        max_length=256, blank=True), default=array_default)
    attributes = ArrayField(models.CharField(
        max_length=256, blank=True), default=array_default)
    vendor = models.CharField(default="", max_length=256, blank=True)
    categories = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    display_y_n = models.CharField(default="", max_length=256, blank=True)
    images_y_n = models.CharField(default="", max_length=256, blank=True)
