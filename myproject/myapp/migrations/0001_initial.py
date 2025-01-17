# Generated by Django 5.0.2 on 2024-03-19 16:01

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Unknown', max_length=50, verbose_name='Product Name')),
                ('product_quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('product_catgories', models.CharField(choices=[('RC', 'Recycable'), ('NRC', 'Non Recycable'), ('RU', 'Reusable'), ('RCV', 'Recover')], default='RC', max_length=3, verbose_name='Catagories')),
                ('manufacturer_name', models.CharField(max_length=50, verbose_name='Company Name')),
                ('manufacture_location', models.CharField(choices=[('Abu Dhabi', 'Abu Dhabi'), ('Dubai', 'Dubai'), ('Ajman', 'Ajman')], default='Abu Dhabi', max_length=50, verbose_name='Location')),
                ('manufacturer_email', models.EmailField(default='', max_length=50, verbose_name='Email')),
                ('manufacturer_phone', models.CharField(default='', max_length=50, verbose_name='Phone')),
                ('manufacturer_address', models.CharField(default='Abu Dhabi', max_length=50, verbose_name='Address')),
                ('product_description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(editable=False, max_length=50, unique=True, verbose_name='Product ID')),
                ('product_name', models.CharField(default='Unknown', max_length=50, verbose_name='Product Name')),
                ('manufacturer_name', models.CharField(default='Unknown', max_length=50, verbose_name='Company Name')),
                ('manufacture_location', models.CharField(default='Abu Dhabi', max_length=50, verbose_name='Location')),
                ('product_type', models.CharField(choices=[('RC', 'Recycable'), ('NRC', 'Non Recycable'), ('RU', 'Reusable'), ('RCV', 'Recover')], default='RC', max_length=50, verbose_name='Product Type')),
                ('product_quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('product_mf_date', models.DateTimeField(auto_now=True, verbose_name='Manufacturing Date')),
                ('product_expiry_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Expiry Date')),
                ('product_ownership', models.CharField(choices=[('SL', 'Seller'), ('US', 'Final User')], default='US', max_length=50, verbose_name='Ownership')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('user_name', models.CharField(max_length=50, verbose_name='User Name')),
                ('telephone_number', models.CharField(max_length=10, verbose_name='Telephone')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Email Id')),
                ('user_catagory', models.CharField(choices=[('SL', 'Seller'), ('US', 'Final User')], default='US', max_length=2, verbose_name='Catagory')),
                ('user_points', models.IntegerField(default=0, verbose_name='Points')),
                ('product_quantity', models.IntegerField(default=0, verbose_name='Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('RC', 'Recycaled'), ('RU', 'Reusing'), ('RCV', 'Recover'), ('NO', 'Not Recyled')], default='NO', max_length=10, verbose_name='Recycle Status')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('product_quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('product', models.ManyToManyField(related_name='who_own_the_product', to='myapp.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.users', verbose_name='User')),
            ],
        ),
    ]
