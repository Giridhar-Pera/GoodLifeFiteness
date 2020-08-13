from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-list')
