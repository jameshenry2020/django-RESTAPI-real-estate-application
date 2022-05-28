from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    ordering = ['email']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["pkid", "id", "email", "first_name", "last_name", "phone", "is_staff", "is_active"]
    list_display_links = [ 'id', 'email']
    list_filter = ['email', 'first_name', 'last_name']
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": ("email", "password",)
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": ("first_name", "last_name", "phone",)
            },
        ),
        (
           _("Permission And Groups"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active")
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to the Henry Real Estate Portal"