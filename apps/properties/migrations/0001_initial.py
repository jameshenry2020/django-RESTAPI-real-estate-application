# Generated by Django 3.2.7 on 2022-06-08 08:34

import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='3 bedroom flat', max_length=200, verbose_name='Property Name')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True)),
                ('description', models.TextField(default='tell us about the property', verbose_name='Property Description')),
                ('ref_code', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Reference Code')),
                ('postal_code', models.CharField(default='120003', max_length=10, verbose_name='Postal Code')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('country', django_countries.fields.CountryField(default='NG', max_length=2, verbose_name='Country')),
                ('city', models.CharField(max_length=200)),
                ('street_address', models.CharField(default='allen avenue, LG.', max_length=255, verbose_name='Street Address')),
                ('property_number', models.IntegerField(default=123, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Property Number')),
                ('tax_fee', models.DecimalField(decimal_places=2, default=0.1, help_text='10% property charged', max_digits=8, verbose_name='Property Tax')),
                ('plot_area', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Plot Area(m^2)')),
                ('total_floors', models.IntegerField(default=0, verbose_name='Number of Floors')),
                ('num_of_bedrooms', models.IntegerField(default=0, verbose_name='Number of Bedrooms')),
                ('num_of_bathrooms', models.IntegerField(default=0, verbose_name='Number of Bathroom')),
                ('amenities', models.CharField(default='swimming pool, kitchen, gym', max_length=200, verbose_name='Other things in the property')),
                ('advert_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent'), ('For Short Stay', 'For Short Stay')], default='For Short Stay', max_length=20, verbose_name='Advert Type')),
                ('property_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Commercial', 'Commercial Building'), ('Office', 'Office Space'), ('WareHouse', 'WareHouse'), ('Other', 'Other')], default='Apartment', max_length=20, verbose_name='What Type of Property')),
                ('cover_photo', models.ImageField(default='/house_sample.jpg', upload_to='', verbose_name='Property Image')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo one')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo two')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo three')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo four')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo five')),
                ('availability_status', models.BooleanField(default=True)),
                ('views', models.IntegerField(default=0, verbose_name='Total Views')),
                ('hosted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='host_agent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyView',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('ip_addr', models.CharField(max_length=255, verbose_name='Ip Address')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_view', to='properties.property')),
            ],
            options={
                'verbose_name': 'Property View',
                'verbose_name_plural': 'Property Views',
            },
        ),
    ]
