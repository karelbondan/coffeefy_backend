from django.db import models

# Create your models here.
class Suggestions(models.Model):
    name = models.CharField(max_length=100)
    suggestion = models.TextField()

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dateAdded = models.DateField()
    price = models.FloatField()

