from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name = name)

        # No clear text password, hasshed password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name, password):
        "Create super user"
        user = self.create_user(email, name, password) # here when we call the create_user function, no need to call the self as it is automatically called


        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    # As we have customized the user model, we need to tell Django how to ineract with the model
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'    # replacing default username feild with a email field
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Reterive full name of user"""
        return self.name

    def get_short_name(self):
        """Reterive short name"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email
