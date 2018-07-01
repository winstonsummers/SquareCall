from django.db import models

# Create your models here.

class Calendar(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    address = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    description = models.TextField()
    flyer = models.ImageField(upload_to='flyers', blank=True, null=True)
    event_site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    #general values
    title = models.CharField(max_length=100)
    text = models.TextField()
    page = models.CharField(max_length=20)
    #location page values
    address = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    #newsletter page values
    letter = models.FileField(upload_to='newsletters', blank=True, null=True)

    def __str__(self):
        return self.title