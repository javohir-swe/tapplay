import re

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models


class CustomUserManager(BaseUserManager):
    # def normalize_phonenumber(self, phone_number):
    #     """Regex for validating +998XXXXXXXXX (13 characters)"""
    #     pattern = r'^\+998\d{9}$'
    #     if not re.match(pattern, phone_number):
    #         raise ValidationError('Phone number must start with +998 and contain exactly 13 characters.')
    #     return phone_number.strip()
    def normalize_phonenumber(self, phone_number):

        return phone_number.strip() if phone_number else phone_number

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Enter phone number')
        phone_number = self.normalize_phonenumber(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    # Django admin paneli uchun zarur metodlarni qo'shamiz
    def has_module_perms(self, app_label):
        """Return True if the user has permissions for the given app label."""
        return self.is_active

    def has_perm(self, perm, obj=None):
        """Return True if the user has the specified permission."""
        return self.is_active
