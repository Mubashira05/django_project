from django.db import models
from django.contrib.auth.models import User

class AnotherModel(models.Model):
    related_user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
