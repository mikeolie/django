# Generated by Django 4.0.3 on 2022-04-13 19:22

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import liberty.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='liberty.category')),
            ],
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor', models.CharField(default='', max_length=120)),
                ('customer', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=120)),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('grade', models.CharField(default='', max_length=120)),
                ('notes', models.TextField(default='')),
                ('admin_notes', models.TextField(default='')),
                ('status', models.CharField(default='', max_length=120)),
                ('sold', models.CharField(default='', max_length=120)),
                ('display_y_n', models.CharField(default='', max_length=120)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('on_hold_till', models.DateTimeField(default=django.utils.timezone.now)),
                ('item_no', models.CharField(max_length=120)),
                ('description', models.CharField(default='', max_length=256)),
                ('total_units', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('avg_cogs', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('profit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('margin', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('mintage', models.IntegerField(default=0)),
                ('pop_known', models.CharField(default='', max_length=100)),
                ('ngc_pop', models.IntegerField(default=0)),
                ('pcgs_pop', models.IntegerField(default=0)),
                ('total_pop', models.IntegerField(default=0)),
                ('finer_known', models.IntegerField(default=0)),
                ('highlights', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=256), default=liberty.models.highlights_default, size=None)),
                ('vendor', models.CharField(default='', max_length=256)),
                ('display_y_n', models.CharField(default='', max_length=256)),
                ('images_y_n', models.CharField(default='', max_length=256)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='liberty.category')),
            ],
        ),
    ]
