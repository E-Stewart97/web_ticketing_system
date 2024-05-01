from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        # Validate the username and password
        if not username:
            raise ValueError(_('The username must be set'))
        if not password:
            raise ValueError(_('The password must be set'))

        user = self.model(
            username=self.normalize_email(username),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_stakeholder', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_employee', True)

        # Validate the extra fields of superuser
        if extra_fields.get('is_employee') is not True:
            raise ValueError(_('Superuser must have is_employee=True.'))
        if extra_fields.get('is_stakeholder') is not True:
            raise ValueError(_('Superuser must have is_stakeholder=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        # Return user as a superuser
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=30, min_length=5, unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    password = models.CharField(max_length=30, min_length=6, blank=False, 
                                validators=[RegexValidator(r'^(?=.*[0-9])(?=.*[!@#$%^&*])[\w!@#$%^&*]+$', 
                                   message="Must contain at least one number and one special character"))
    username = models.CharField(max_length=30, min_length=5, unique=True, blank=False)  
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_employee] 

    objects = UserManager()

    def __str__(self):
        return self.username
