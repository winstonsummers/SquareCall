from django.db import models

# Create your models here.

class Calendar(models.Model):
    date_time = models.DateTimeField()
    address = models.CharField()
    venue = models.CharField()
    description = models.TextField()
    flyer = models.ImageField(upload_to='flyers')
    event_site = models.URLField()

class Post(models.Model):
    #general values
    title = models.CharField()
    text = models.TextField()
    page = models.CharField()
    #location page values
    address = models.CharField()
    venue = models.CharField()
    #newsletter page values
    letter = models.FileField(upload_to='newsletters')