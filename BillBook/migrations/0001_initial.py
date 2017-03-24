# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('mobile_no_1', models.IntegerField(blank=True, null=True)),
                ('mobile_no_2', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BillBook.Customer'),
        ),
    ]
