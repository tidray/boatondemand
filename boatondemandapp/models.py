from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='manager_logo/', blank=False)

    def __str__(self):
        return self.name
