from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=22)
    description=models.TextField(max_length=100)