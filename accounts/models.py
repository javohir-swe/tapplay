from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    class UserRole(models.TextChoices):
        USER = "USER", _("User")
        AUTHOR = "AUTHOR", _("Author")
        ADMIN = "ADMIN", _("Admin")

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True)
    bookmark = models.ManyToManyField("audio.Audio", related_name="bookmarked_by", blank=True)

    user_role = models.CharField(choices=UserRole, default=UserRole.USER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    # Django admin paneli uchun zarur metodlarni qo'shamiz
    def has_module_perms(self, app_label):
        """Return True if the user has permissions for the given app label."""
        return self.is_active

    def has_perm(self, perm, obj=None):
        """Return True if the user has the specified permission."""
        return self.is_active

# Foydalanuvchining saqlagan audio fayllari
# user.bookmark.all()

# Har bir audio faylni saqlagan foydalanuvchilar
# audio.bookmarked_by.all()
