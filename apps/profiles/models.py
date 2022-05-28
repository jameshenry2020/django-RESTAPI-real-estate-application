from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField
from apps.users.models import CommonUUIDModel

User=get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")


class Profile(CommonUUIDModel):
    user=models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me=models.TextField(verbose_name=_("About me"), default="tell us about yourself")
    profile_img=models.ImageField(verbose_name=_("Profile Image"), default="/profile_img.png")
    gender=models.CharField(max_length=7, verbose_name=_("Gender"), choices=Gender.choices, default=Gender.MALE)
    country=CountryField(default="NG", verbose_name=_("Country"))
    city = models.CharField(max_length=50, default="Lagos", verbose_name=_("City"))
    is_agent = models.BooleanField(default=False, help_text=_("Are you an Agent ?"), verbose_name=_("Agent"))

    def __str__(self):
        return f"{self.user.first_name} profile"


