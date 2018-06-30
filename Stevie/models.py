from django.db import models

# Create your models here.

class Calendar(models.Model):
    date_time = models.DateTimeField()
    address = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    description = models.TextField()
    flyer = models.ImageField(upload_to='flyers')
    event_site = models.URLField()

class Post(models.Model):
    #general values
    title = models.CharField(max_length=100)
    text = models.TextField()
    page = models.CharField(max_length=20)
    #location page values
    address = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    #newsletter page values
    letter = models.FileField(upload_to='newsletters')