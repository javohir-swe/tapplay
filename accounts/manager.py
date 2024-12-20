from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def normalize_phonenumber(self, phone_number):
        return phone_number.strip() if phone_number else phone_number

    def create_user(self, username, password=None, phone_number=None, **extra_fields):
        if not username:
            raise ValueError('Enter username')
        phone_number = self.normalize_phonenumber(phone_number)
        user = self.model(username=username, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
