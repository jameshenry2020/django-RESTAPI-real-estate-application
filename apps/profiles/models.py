from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.users.models import CommonUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")


class Profile(CommonUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me = models.TextField(
        verbose_name=_("About me"), default="tell us about yourself"
    )
    profile_img = models.ImageField(
        verbose_name=_("Profile Image"), default="/profile_img.png"
    )
    gender = models.CharField(
        max_length=7,
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.MALE,
    )
    country = CountryField(default="NG", verbose_name=_("Country"))
    city = models.CharField(max_length=50, default="Lagos", verbose_name=_("City"))
    is_agent = models.BooleanField(
        default=False, help_text=_("Are you an Agent ?"), verbose_name=_("Agent")
    )

    def __str__(self):
        return f"{self.user.first_name} profile"


class HostAgent(CommonUUIDModel):
    brand_name = models.CharField(
        max_length=200, verbose_name=_("Host Business Name"), unique=True
    )
    profile = models.ForeignKey(
        Profile, related_name="agent", on_delete=models.DO_NOTHING
    )
    license = models.CharField(
        verbose_name=_("Real Estate License"), max_length=30, blank=True, null=True
    )
    office_address = models.CharField(max_length=400, verbose_name=_("Office Address"))
    num_of_reviews = models.IntegerField(default=0, verbose_name=_("Number of Reviews"))

    def __str__(self):
        return self.brand_name
