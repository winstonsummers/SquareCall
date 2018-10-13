from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venues', views.venues, name='venues'),
    path('calendar', views.calendar, name='calendar'),
    path('essense', views.essense, name="essense"),
    path('newsnnotes', views.newsnnotes, name="newsnnotes")
]