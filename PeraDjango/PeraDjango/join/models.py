from django.db import models


# Create your models here.

class Join(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField
    email = models.CharField
