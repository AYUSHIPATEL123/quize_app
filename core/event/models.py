from django.db import models
from django.utils import timezone
# Create your models here.

# Event model definition
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):   # __str__ method
        return self.title
    
