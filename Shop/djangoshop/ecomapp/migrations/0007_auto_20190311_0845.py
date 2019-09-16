# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-11 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_auto_20190311_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='buying_types',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=40),
        ),
    ]