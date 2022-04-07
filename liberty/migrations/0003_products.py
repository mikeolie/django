# Generated by Django 4.0.3 on 2022-04-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberty', '0002_test_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField()),
                ('on_hold_till', models.DateTimeField()),
                ('item_no', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
    ]
