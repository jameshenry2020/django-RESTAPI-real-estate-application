from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings
from apps.users.models import CommonUUIDModel
from apps.profiles.models import HostAgent
from apps.properties.models import Property


class Rating(CommonUUIDModel):

    class RatingChoice(models.IntegerChoices):
        Rating_1 = 1, _("Poor")
        Rating_2 = 2, _("Fair")
        Rating_3 = 3, _("Good")
        Rating_4 = 4, _("Very Good")
        Rating_5 = 5, _("Excellent")

    client = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User providing the Rating"), on_delete=models.SET_NULL, null=True)
    agent=models.ForeignKey(HostAgent, verbose_name=_("Agent receiving the review"), on_delete=models.SET_NULL, null=True)
    rating=models.IntegerField(verbose_name=_("Rating"), choices=RatingChoice.choices, default=0)
    comment=models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["client", "agent"]

    def __str__(self):
        return f"{self.properte} rated"




