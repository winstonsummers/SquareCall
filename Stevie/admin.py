from django.contrib import admin
from .models import Calendar, Post


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'venue')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'venue')

# Register your models here.
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Post, PostAdmin)