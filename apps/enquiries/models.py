from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.properties.models import Property
from apps.users.models import CommonUUIDModel

# Create your models here.


class EnquiryRequest(CommonUUIDModel):
    property = models.ForeignKey(
        Property, related_name="enquiry", on_delete=models.DO_NOTHING
    )
    names = models.CharField(max_length=255, verbose_name=_("Your Name"))
    email = models.EmailField(verbose_name=_("Email Address"))
    phone = PhoneNumberField(_("Phone Number"), max_length=20, default="+2349035467822")
    message = models.TextField(_("Message"))

    def __str__(self):
        return f"enquiry for {self.property.title} in {self.property.city}"

    class Meta:
        verbose_name_plural = "Enquiries"
