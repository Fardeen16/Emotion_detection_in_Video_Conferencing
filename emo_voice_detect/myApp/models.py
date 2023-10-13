from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    neutral = models.FloatField()
    happy = models.FloatField()
    sad = models.FloatField()
    angry = models.FloatField()
    disgusted = models.FloatField()
    surprised = models.FloatField()
    fearful = models.FloatField()

    REQUIRED_FIELDS = []
