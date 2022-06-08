import random
import string
from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings
from apps.users.models import CommonUUIDModel


User=get_user_model()

class PropertyAvailabilityManager(models.Manager):
    def get_queryset(self):
        return (
                super(PropertyAvailabilityManager, self)
                .get_queryset()
                .filter(availability_status=True)
                )

class Property(CommonUUIDModel):
    class AdvertType(models.TextChoices):
        FOR_SALE = "For Sale", _("For Sale")
        FOR_RENT = "For Rent", _("For Rent")
        FOR_SHORT_STAY ="For Short Stay", _("For Short Stay")

    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        COMMERCIAL = "Commercial", _("Commercial Building")
        OFFICE = "Office", _("Office Space")
        WAREHOUSE = "WareHouse", _("WareHouse")
        OTHER = "Other", _("Other")


    title = models.CharField(max_length=200, default="3 bedroom flat", verbose_name=_("Property Name"))
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    hosted_by = models.ForeignKey(User, related_name="host_agent", on_delete=models.DO_NOTHING)
    description = models.TextField(verbose_name= _("Property Description"), default="tell us about the property")
    ref_code = models.CharField(max_length=10, unique=True, verbose_name=_("Reference Code"), blank=True)
    postal_code = models.CharField(max_length=10, default="120003", verbose_name=_("Postal Code"))
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    country = CountryField(verbose_name=_("Country"), default="NG", blank_label="(Select Country)" )
    city = models.CharField(max_length=200)
    street_address = models.CharField(max_length=255, verbose_name=_("Street Address"), default="allen avenue, LG.")
    property_number = models.IntegerField(verbose_name=_("Property Number"), validators=[MinValueValidator(1)], default=123)
    tax_fee = models.DecimalField(verbose_name=_("Property Tax"), max_digits=8, decimal_places=2, default=0.10, help_text="10% property charged")
    plot_area = models.DecimalField(verbose_name=_("Plot Area(m^2)"), max_digits=8, decimal_places=2, default=0.0)
    total_floors = models.IntegerField(verbose_name=_("Number of Floors"), default=0)
    num_of_bedrooms = models.IntegerField(verbose_name=_("Number of Bedrooms"), default=0)
    num_of_bathrooms = models.IntegerField(verbose_name=_("Number of Bathroom"), default=0)
    amenities = models.CharField(max_length=200, verbose_name=_("Other things in the property"), default="swimming pool, kitchen, gym")
    advert_type = models.CharField(max_length=20, verbose_name=_("Advert Type"), choices=AdvertType.choices, default=AdvertType.FOR_SHORT_STAY)
    property_type = models.CharField(max_length=20, verbose_name=_("What Type of Property"), choices=PropertyType.choices, default=PropertyType.APARTMENT)
    cover_photo = models.ImageField(verbose_name=_("Property Image"), default="/house_sample.jpg")
    photo1 = models.ImageField(verbose_name=_("photo one"),  blank=True, null=True)
    photo2 = models.ImageField(verbose_name=_("photo two"), blank=True, null=True)
    photo3 = models.ImageField(verbose_name=_("photo three"), blank=True, null=True)
    photo4 = models.ImageField(verbose_name=_("photo four"), blank=True, null=True)
    photo5 = models.ImageField(verbose_name=_("photo five"), blank=True, null=True)
    availability_status = models.BooleanField(default=True)
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    objects = models.Manager()
    available = PropertyAvailabilityManager()

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name="Property"
        verbose_name_plural = "Properties"


    def save(self, *args, **kwargs):
        self.ref_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        tax_percentage = self.tax_fee
        property_price = self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price + tax_amount, 2))
        return price_after_tax

    
class PropertyView(CommonUUIDModel):
    ip_addr = models.CharField(max_length=255, verbose_name=_("Ip Address"))
    property=models.ForeignKey(Property, related_name="property_view", on_delete=models.CASCADE)

    def __str__(self):
        return f"Total views on {self.property.title} is {self.property.views}"

    class Meta:
        verbose_name= "Property View"
        verbose_name_plural ="Property Views"



    

    
