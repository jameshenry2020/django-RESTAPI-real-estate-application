from django.contrib import admin
from .models import Profile, HostAgent


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "gender", "country", "city"]
    list_filter= ["gender", "country", "city"]
    list_display_link = ["pkid", "id", "user"]


class HostAgentAdmin(admin.ModelAdmin):
    list_display = ["id", "brand_name", "license"]
    list_display_links = ["id", "brand_name"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(HostAgent, HostAgentAdmin)



