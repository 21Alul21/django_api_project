from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
import uuid

# Create your models here.

class CustomBaseUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email cannot be empty')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') != True:
            raise ValueError('is_staff must be set to True')
        if extra_fields.get('is_staff') != True:
            raise ValueError('is_staff must be set to True')
        
        return self.create_user(email=email, password=password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    userId = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    firstName = models.CharField(max_length=125, null=False)
    lastName = models.CharField(max_length=125, null=False)
    email = models.EmailField(max_length=125, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=125, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomBaseUserManager()

class Organisation(models.Model):
    orgId = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=125, null=False)
    description = models.TextField()
    organization = models.ManyToManyField(User)


    