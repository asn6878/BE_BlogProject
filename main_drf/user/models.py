from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)

    def __str__(self):
        return self.username
    
