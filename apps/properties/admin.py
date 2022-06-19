from django.contrib import admin
from .models import  Property, PropertyView


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "country", "city", "advert_type", "price"]
    list_display_links = ["title"]
    list_filter = ["title", "country", "city"]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyView)
