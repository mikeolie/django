# Generated by Django 4.0.3 on 2022-04-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberty', '0005_requestlog_alter_products_display_y_n_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='display_y_n',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='products',
            name='images_y_n',
            field=models.CharField(default='', max_length=256),
        ),
    ]
