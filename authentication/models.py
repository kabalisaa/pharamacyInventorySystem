from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.
class User(AbstractUser):
    USER_CHOICE = [
        ('admin', 'admin'),
        ('pharmacist', 'pharmacist'),
        ('supplier', 'supplier'),
    ]
    email = models.EmailField(verbose_name="User Email", max_length=255, unique=True)
    user_type = models.CharField(verbose_name="User Type", choices=USER_CHOICE, max_length=50)
    username = None
    first_name = None
    last_name = None
    
    object = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['user_type',]
    
    def  __str__(self):
        return self.email