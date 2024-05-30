# events/models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
