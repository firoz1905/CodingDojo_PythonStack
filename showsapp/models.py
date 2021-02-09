from django.db import models
from datetime import datetime

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateTimeField()
    desc=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)