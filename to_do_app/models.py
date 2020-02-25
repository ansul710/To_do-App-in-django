import datetime

from django.db import models


# Create your models here.

class TodoItems(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
