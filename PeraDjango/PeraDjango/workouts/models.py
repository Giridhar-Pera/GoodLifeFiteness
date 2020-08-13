from django.db import models


# Create your models here.

class Workouts(models.Model):
    Type = models.CharField(max_length=120, null=True)
    Exercises = models.CharField(max_length=120, null=True)
    Muscles_Involved = models.CharField(max_length=120, null=True)
    Description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.Type
