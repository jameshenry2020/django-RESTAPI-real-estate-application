# Generated by Django 3.2.7 on 2022-06-11 16:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0002_alter_property_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryRequest',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('names', models.CharField(max_length=255, verbose_name='Your Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+2349035467822', max_length=20, region=None, verbose_name='Phone Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enquiry', to='properties.property')),
            ],
            options={
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]