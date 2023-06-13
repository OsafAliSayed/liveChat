from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Table that holds user data
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=100)
    isadmin = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}, {self.username}, {self.email}"