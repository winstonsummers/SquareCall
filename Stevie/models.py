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

    def getMonth(self):
        return self.date_time.strftime('%b')

    def dayOfWeek(self):
        return self.date_time.strftime('%a')

    def dateAndDay(self):
        return self.dayOfWeek() + " " + str(self.date_time.day)

    def __str__(self):
        return self.title

class Post(models.Model):
    HOME = 'HM'
    VENUES = 'VN'
    CALENDAR = 'CL'
    ESSENSE = 'ES'
    SIDEBAR = 'SB'
    CONTACT_INFO = 'CI'
    NEWSN_NOTES = 'NN'
    PAGE_INDEX = (
        (HOME, 'Home'),
        (VENUES, 'Venues'),
        (CALENDAR, 'Calendar'),
        (ESSENSE, 'esSense'),
        (SIDEBAR, 'Sidebar'),
        (CONTACT_INFO, 'Contact Info'),
        (NEWSN_NOTES, 'NEWS\'n NOTES')
    )
    #general values
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    page = models.CharField(max_length=2, choices=PAGE_INDEX)
    #location page values
    address = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    #newsletter page values
    letter = models.FileField(upload_to='newsletters', blank=True, null=True)

    def __str__(self):
        return self.title