from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "gender", "country", "city"]
    list_filter= ["gender", "country", "city"]
    list_display_link = ["pkid", "id", "user"]


admin.site.register(Profile, ProfileAdmin)



