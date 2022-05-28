from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings
from apps.users.models import CommonUUIDModel



class Property(CommonUUIDModel):
    property_type=models.CharField(max_length=200, default="apartment", verbose_name=_("What kind of Place"))
    description=models.TextField()
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.property_type} in {self.city}"
