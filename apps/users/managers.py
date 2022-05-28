from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('you must provide a valid email address'))

    def create_user(self, email, first_name, last_name, phone, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Base User Account: An email address is required'))

        if not first_name:
            raise ValueError(_('First name is required'))
        if not last_name:
            raise ValueError(_('Last name is required'))
        if not phone:
            raise ValueError(_('phone number is required'))

        user = self.model(
            email=email, 
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_('is staff must be true for admin user'))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_('is superuser must be true for admin user'))

        user = self.create_user(email, first_name, last_name, phone, password, **extra_fields)
        user.save(using=self._db)
        return user

