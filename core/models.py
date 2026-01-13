from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    position = models.CharField(max_length=255, blank=True, null=True)
    imgProfile = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username

